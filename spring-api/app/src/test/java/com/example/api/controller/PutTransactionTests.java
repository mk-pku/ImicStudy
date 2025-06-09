package com.example.api.controller;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import com.example.api.BaseIntegrationTest;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;

import java.util.Map;

class PutTransactionTests extends BaseIntegrationTest {

	private String toJson(Object dto) {
		try {
			return new com.fasterxml.jackson.databind.ObjectMapper().writeValueAsString(dto);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	@Test
	void testPutTransactionSuccess() throws Exception {
		int txnId = 1;
		var payload = Map.of(
			"date", "2025-06-05",
			"category_id", 18,
			"memo", "PUT - 給料2",
			"income", 1000000,
			"expenditure", 0
		);

		mockMvc.perform(put("/api/transactions/{id}", txnId)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isOk())
			.andExpect(jsonPath("$.id").value(txnId))
			.andExpect(jsonPath("$.date").value("2025-06-05"))
			.andExpect(jsonPath("$.category_id").value(18))
			.andExpect(jsonPath("$.memo").value("PUT - 給料2"))
			.andExpect(jsonPath("$.income").value(1000000))
			.andExpect(jsonPath("$.expenditure").value(0));
	}

	@Test
	void testPutTransactionInvalidField() throws Exception {
		int txnId = 1;
		var payload = Map.of(
			"date", "2025/06/05",
			"category_id", 18,
			"memo", "日付形式エラー",
			"income", 1000000,
			"expenditure", 0
		);

		mockMvc.perform(put("/api/transactions/{id}", txnId)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isBadRequest());
	}

	@Test
	void testPutTransactionMissingField() throws Exception {
		int txnId = 1;
		var payload = Map.of(
			"category_id", 18,
			"memo", "日付なし",
			"income", 1000000,
			"expenditure", 0
		);

		mockMvc.perform(put("/api/transactions/{id}", txnId)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isBadRequest());
	}

	@Test
	void testPutTransactionNonexistentCategory() throws Exception {
		int txnId = 1;
		var payload = Map.of(
			"date", "2025-06-05",
			"category_id", 9999,
			"memo", "カテゴリなしエラー",
			"income", 1000000,
			"expenditure", 0
		);

		mockMvc.perform(put("/api/transactions/{id}", txnId)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isBadRequest());
	}

	@Test
	void testPutTransactionNotFound() throws Exception {
		var payload = Map.of(
			"date", "2025-06-05",
			"category_id", 1,
			"memo", "存在しないID",
			"income", 1000000,
			"expenditure", 0
		);

		mockMvc.perform(put("/api/transactions/{id}", 9999)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isNotFound());
	}
}
