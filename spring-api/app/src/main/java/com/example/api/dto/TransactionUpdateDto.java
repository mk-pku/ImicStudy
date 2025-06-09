package com.example.api.dto;

import java.time.LocalDate;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class TransactionUpdateDto {
	@NotNull LocalDate date;
	@NotNull @Min(1) Integer categoryId;
	@Min(0) Integer income;
	@Min(0) Integer expenditure;
	String memo;
}
