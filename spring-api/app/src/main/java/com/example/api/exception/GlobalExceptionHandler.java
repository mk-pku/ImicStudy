package com.example.api.exception;

import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ProblemDetail;
import org.springframework.http.ResponseEntity;
import org.springframework.lang.NonNull;
import org.springframework.validation.FieldError;
import org.springframework.web.ErrorResponse;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.ServletWebRequest;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import java.time.LocalDateTime;
import java.util.stream.Collectors;

/**
 * コントローラ層の例外を一括処理するハンドラ
 */
@ControllerAdvice
public class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

	/** 400 Validation Errors */
	@Override
	@NonNull
	protected ResponseEntity<Object> handleMethodArgumentNotValid(
			@NonNull MethodArgumentNotValidException ex,
			@NonNull HttpHeaders headers,
			@NonNull HttpStatusCode status,
			@NonNull WebRequest request) {

		String detail = ex.getBindingResult().getFieldErrors().stream()
				.map(FieldError::getDefaultMessage)
				.collect(Collectors.joining("; "));
		
		ProblemDetail pd = ProblemDetail.forStatus(status.value());
		pd.setDetail(detail);
	
		pd.setProperty("timestamp", LocalDateTime.now());
		pd.setProperty("path", ((ServletWebRequest) request)
				.getRequest().getRequestURI());

		return ResponseEntity.status(status).headers(headers).body(pd);
  	}

	/** 400 DB 制約違反（外部キーなど） */
    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity<ProblemDetail> handleDataIntegrityViolation(
            DataIntegrityViolationException ex,
            WebRequest request) {
		
		ResponseStatusException rse = new ResponseStatusException(
				HttpStatus.BAD_REQUEST, "指定された categoryId は存在しません");
		ProblemDetail pd = ((ErrorResponse) rse).getBody();

		pd.setProperty("timestamp", LocalDateTime.now());
		pd.setProperty("path", ((ServletWebRequest) request).getRequest().getRequestURI());
		
		return ResponseEntity.badRequest().headers(rse.getHeaders()).body(pd);
    }

	/** 404 リソース未検出 */
	@ExceptionHandler(ResourceNotFoundException.class)
	public ResponseEntity<ProblemDetail> handleNotFound(
			ResourceNotFoundException ex, WebRequest request) {

		ResponseStatusException rse = new ResponseStatusException(
			HttpStatus.NOT_FOUND, ex.getMessage());
		ProblemDetail pd = ((ErrorResponse) rse).getBody();

		pd.setProperty("timestamp", LocalDateTime.now());
		pd.setProperty("path",
			((ServletWebRequest) request).getRequest().getRequestURI());
		
		return ResponseEntity.status(HttpStatus.NOT_FOUND).headers(rse.getHeaders()).body(pd);
	}

	/** 500 その他予期せぬエラー */
	@ExceptionHandler(ResponseStatusException.class)
	public ResponseEntity<ProblemDetail> handleResponseStatus(
			ResponseStatusException ex,
			WebRequest request) {

		ProblemDetail pd = ((ErrorResponse) ex).getBody();
		pd.setProperty("timestamp", LocalDateTime.now());
		pd.setProperty("path", ((ServletWebRequest) request).getRequest().getRequestURI());

		return ResponseEntity.status(ex.getStatusCode()).headers(ex.getHeaders()).body(pd);
  	}
}
