package com.example.api.model;

import java.time.LocalDate;
import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Transaction {
	private Integer id;
	private LocalDate date;
	private Integer categoryId;
	private String memo;
	private Integer income;
	private Integer expenditure;
	private LocalDateTime createdAt;
	private LocalDateTime updatedAt;
}
