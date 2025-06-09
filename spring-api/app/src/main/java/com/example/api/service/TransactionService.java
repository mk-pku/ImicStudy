package com.example.api.service;

import java.util.List;
import com.example.api.dto.TransactionCreateDto;
import com.example.api.dto.TransactionPatchDto;
import com.example.api.dto.TransactionUpdateDto;
import com.example.api.dto.TransactionResponseDto;

public interface TransactionService {
    List<TransactionResponseDto> getAll();
	TransactionResponseDto getById(Integer id);
	TransactionResponseDto create(TransactionCreateDto dto);
	TransactionResponseDto update(Integer id, TransactionUpdateDto dto);
	TransactionResponseDto patch(Integer id, TransactionPatchDto dto);
	void delete(Integer id);
}
