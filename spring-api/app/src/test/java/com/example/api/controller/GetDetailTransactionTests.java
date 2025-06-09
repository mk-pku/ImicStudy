package com.example.api.controller;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.*;

import com.example.api.BaseIntegrationTest;
import org.junit.jupiter.api.Test;

class GetDetailTransactionTests extends BaseIntegrationTest {

	/** 正常系 */
	@Test
	void testGetDetailTransactionSuccess() throws Exception {
		int txnId = 1;
		mockMvc.perform(get("/api/transactions/{id}", txnId))
			.andDo(print())
			.andExpect(status().isOk())
			.andExpect(jsonPath("$.id").value(txnId))
			.andExpect(jsonPath("$.date").value("2025-06-01"))
			.andExpect(jsonPath("$.category_id").value(1))
			.andExpect(jsonPath("$.memo").value("Base - 趣味・娯楽1"))
			.andExpect(jsonPath("$.income").value(0))
			.andExpect(jsonPath("$.expenditure").value(5000));
	}

	/** 異常系: 存在しない ID */
	@Test
	void testGetDetailTransactionNotFound() throws Exception {
		mockMvc.perform(get("/api/transactions/{id}", 9999))
			.andDo(print())
			.andExpect(status().isNotFound());
	}
}
