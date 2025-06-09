package com.example.api.dto;

import java.time.LocalDate;
import jakarta.validation.constraints.NotNull;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class TransactionUpdateDto {
	@NotNull(message = "date は必須項目です")
	private LocalDate date;

	@NotNull(message = "categoryId は必須項目です")
	private Integer categoryId;

	private String memo;
	private Integer income;
	private Integer expenditure;
	
}
