package com.example.api.model;

import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Category {
	private Integer id;
	private String name;
	private String notes;
	private LocalDateTime createdAt;
	private LocalDateTime updatedAt;
}
