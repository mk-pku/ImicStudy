package com.example.api.mapper;

import java.util.List;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import com.example.api.model.Transaction;

@Mapper
public interface TransactionMapper {
	List<Transaction> findAll();
	Transaction findById(@Param("id") Integer id);
	int insert(Transaction Transaction);
	int update(Transaction Transaction);
	int deleteById(@Param("id") Integer id);
	int patch(@Param("id") Integer id,
			@Param("date") java.time.LocalDate date,
			@Param("categoryId") Integer categoryId,
			@Param("memo") String memo,
			@Param("income") Integer income,
			@Param("expenditure") Integer expenditure);
}
