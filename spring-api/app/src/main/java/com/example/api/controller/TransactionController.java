package com.example.api.controller;

import java.util.List;
import jakarta.validation.Valid;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.example.api.dto.TransactionCreateDto;
import com.example.api.dto.TransactionPatchDto;
import com.example.api.dto.TransactionUpdateDto;
import com.example.api.dto.TransactionResponseDto;
import com.example.api.service.TransactionService;

@RestController
@RequestMapping("/api/transactions")
public class TransactionController {

	private final TransactionService transactionService;

	public TransactionController(TransactionService transactionService) {
		this.transactionService = transactionService;
	}

	/**
	 * 全件取得
	 * GET /api/transactions
	 */
	@GetMapping
	public ResponseEntity<List<TransactionResponseDto>> getAll() {
		List<TransactionResponseDto> list = transactionService.getAll();
		return ResponseEntity.ok(list);
	}

	/**
	 * ID で詳細取得
	 * GET /api/transactions/{id}
	 */
	@GetMapping("/{id}")
	public ResponseEntity<TransactionResponseDto> getById(@PathVariable Integer id) {
		TransactionResponseDto dto = transactionService.getById(id);
		return ResponseEntity.ok(dto);
	}

	/**
	 * 新規登録
	 * POST /api/transactions
	 */
	@PostMapping
	public ResponseEntity<TransactionResponseDto> create(
			@Valid @RequestBody TransactionCreateDto createDto) {

		TransactionResponseDto created = transactionService.create(createDto);
		return ResponseEntity.status(HttpStatus.CREATED).body(created);
	}

	/**
	 * 全項目更新（置き換え）
	 * PUT /api/transactions/{id}
	 */
	@PutMapping("/{id}")
	public ResponseEntity<TransactionResponseDto> update(
			@PathVariable Integer id,
			@Valid @RequestBody TransactionUpdateDto updateDto) {

		TransactionResponseDto updated = transactionService.update(id, updateDto);
		return ResponseEntity.ok(updated);
	}

	/**
	 * 部分更新（PATCH）
	 * PATCH /api/transactions/{id}
	 */
	@PatchMapping("/{id}")
	public ResponseEntity<TransactionResponseDto> patch(
			@PathVariable Integer id,
			@Valid @RequestBody TransactionPatchDto patchDto) {

		TransactionResponseDto patched = transactionService.patch(id, patchDto);
		return ResponseEntity.ok(patched);
	}

	/**
	 * 削除
	 * DELETE /api/transactions/{id}
	 */
	@DeleteMapping("/{id}")
	public ResponseEntity<Void> delete(@PathVariable Integer id) {
		transactionService.delete(id);
		return ResponseEntity.noContent().build();
	}
}
