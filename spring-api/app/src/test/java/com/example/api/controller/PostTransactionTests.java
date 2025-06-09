package com.example.api.controller;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import com.example.api.BaseIntegrationTest;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;

import java.util.Map;

class PostTransactionTests extends BaseIntegrationTest {

	private String toJson(Object dto) {
		try {
			return new com.fasterxml.jackson.databind.ObjectMapper().writeValueAsString(dto);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	@Test
	void testPostTransactionSuccess() throws Exception {
		var payload = Map.of(
			"date", "2025-06-01",
			"category_id", 18,
			"memo", "［テスト投稿］映画鑑賞",
			"income", 0,
			"expenditure", 2000
		);

		mockMvc.perform(post("/api/transactions")
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isCreated());
	}

	@Test
	void testPostTransactionMissingField() throws Exception {
		var payload = Map.of(
			"category_id", 1,
			"memo", "日付なしエラー",
			"income", 200000,
			"expenditure", 0
		);

		mockMvc.perform(post("/api/transactions")
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isBadRequest());
	}

	@Test
	void testPostTransactionInvalidDateFormat() throws Exception {
		var payload = Map.of(
			"date", "2025/06/30",
			"category_id", 1,
			"memo", "日付形式エラー",
			"income", 200000,
			"expenditure", 0
		);

		mockMvc.perform(post("/api/transactions")
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isBadRequest());
	}

	@Test
	void testPostTransactionNonexistentCategory() throws Exception {
		var payload = Map.of(
			"date", "2025-06-30",
			"category_id", 9999,
			"memo", "カテゴリなしエラー",
			"income", 200000,
			"expenditure", 0
		);

		mockMvc.perform(post("/api/transactions")
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isBadRequest());
	}
}
