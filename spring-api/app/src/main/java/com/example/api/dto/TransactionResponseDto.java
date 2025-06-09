package com.example.api.dto;

import java.time.LocalDate;
import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class TransactionResponseDto {
	private Integer id;
	private LocalDate date;
	private Integer categoryId;
	private String memo;
	private Integer income;
	private Integer expenditure;
	private LocalDateTime createdAt;
	private LocalDateTime updatedAt;   
}
