package com.example.api.service.impl;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.example.api.dto.TransactionCreateDto;
import com.example.api.dto.TransactionUpdateDto;
import com.example.api.dto.TransactionResponseDto;
import com.example.api.exception.ResourceNotFoundException;
import com.example.api.mapper.TransactionMapper;
import com.example.api.model.Transaction;
import com.example.api.service.TransactionService;

@Service
@Transactional
public class TransactionServiceImpl implements TransactionService {
	private final TransactionMapper transactionMapper;

	public TransactionServiceImpl(TransactionMapper transactionMapper) {
		this.transactionMapper = transactionMapper;
	}

	@Override
	@Transactional(readOnly = true)
	public List<TransactionResponseDto> getAll() {
		return transactionMapper.findAll()
			.stream()
			.map(this::toResponseDto)
			.collect(Collectors.toList());
	}

	@Override
	@Transactional(readOnly = true)
	public TransactionResponseDto getById(Integer id) {
		Transaction entity = transactionMapper.findById(id);
		if (entity == null) {
			throw new ResourceNotFoundException("Transaction not found with id: " + id);
		}
		return toResponseDto(entity);
	}

	@Override
	public TransactionResponseDto create(TransactionCreateDto dto) {
		Transaction entity = Transaction.builder()
			.date(dto.getDate())
			.categoryId(dto.getCategoryId())
			.memo(dto.getMemo())
			.income(dto.getIncome())
			.expenditure(dto.getExpenditure())
			.build();

		transactionMapper.insert(entity);
		// insert 後、自動採番された ID が entity.id にセット済み
		return toResponseDto(entity);
	}

	@Override
	public TransactionResponseDto update(Integer id, TransactionUpdateDto dto) {
		// 存在チェック
		Transaction existing = transactionMapper.findById(id);
		if (existing == null) {
			throw new ResourceNotFoundException("Transaction not found with id: " + id);
		}
		existing.setDate(dto.getDate());
		existing.setCategoryId(dto.getCategoryId());
		existing.setMemo(dto.getMemo());
		existing.setIncome(dto.getIncome());
		existing.setExpenditure(dto.getExpenditure());
		transactionMapper.update(existing);
		return toResponseDto(existing);
	}

	@Override
	public TransactionResponseDto patch(Integer id, TransactionUpdateDto dto) {
		// 存在チェック
		Transaction existing = transactionMapper.findById(id);
		if (existing == null) {
			throw new ResourceNotFoundException("Transaction not found with id: " + id);
		}
		// DTO の各フィールドが null でない場合にのみ更新
		transactionMapper.patch(
			id,
			dto.getDate(),
			dto.getCategoryId(),
			dto.getMemo(),
			dto.getIncome(),
			dto.getExpenditure()
		);
		// 更新後の状態を再取得
		Transaction updated = transactionMapper.findById(id);
		return toResponseDto(updated);
	}

	@Override
	public void delete(Integer id) {
		Transaction existing = transactionMapper.findById(id);
		if (existing == null) {
			throw new ResourceNotFoundException("Transaction not found with id: " + id);
		}
		transactionMapper.deleteById(id);
	}

	/** エンティティ → レスポンス DTO 変換ユーティリティ */
	private TransactionResponseDto toResponseDto(Transaction entity) {
		return new TransactionResponseDto(
			entity.getId(),
			entity.getDate(),
			entity.getCategoryId(),
			entity.getMemo(),
			entity.getIncome(),
			entity.getExpenditure(),
			entity.getCreatedAt(),
			entity.getUpdatedAt()
		);
	}
}
