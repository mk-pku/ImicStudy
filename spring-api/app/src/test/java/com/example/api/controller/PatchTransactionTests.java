package com.example.api.controller;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import com.example.api.BaseIntegrationTest;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;

import java.util.Map;

class PatchTransactionTests extends BaseIntegrationTest {

	private String toJson(Object dto) {
		// Jackson ObjectMapper を使う例
		try {
			return new com.fasterxml.jackson.databind.ObjectMapper().writeValueAsString(dto);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	@Test
	void testPatchTransactionSuccess() throws Exception {
		int txnId = 1;
		var payload = Map.of("memo", "PATCH - 映画鑑賞");

		mockMvc.perform(patch("/api/transactions/{id}", txnId)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isOk())
			.andExpect(jsonPath("$.id").value(txnId))
			.andExpect(jsonPath("$.memo").value("PATCH - 映画鑑賞"));
	}

	@Test
	void testPatchTransactionInvalidField() throws Exception {
		int txnId = 1;
		var payload = Map.of("income", -100);

		mockMvc.perform(patch("/api/transactions/{id}", txnId)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isBadRequest());
	}

	@Test
	void testPatchTransactionNotFound() throws Exception {
		var payload = Map.of("memo", "存在しないID");

		mockMvc.perform(patch("/api/transactions/{id}", 8888)
				.contentType(MediaType.APPLICATION_JSON)
				.content(toJson(payload)))
			.andExpect(status().isNotFound());
	}
}
