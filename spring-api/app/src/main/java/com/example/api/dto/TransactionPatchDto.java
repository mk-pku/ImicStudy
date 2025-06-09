package com.example.api.dto;

import java.time.LocalDate;

import jakarta.validation.constraints.Min;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class TransactionPatchDto {
	LocalDate date;
	@Min(1) Integer categoryId;
	@Min(0) Integer income;
	@Min(0) Integer expenditure;
	String memo;
}
