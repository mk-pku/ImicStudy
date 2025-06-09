package com.example.api.controller;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import com.example.api.BaseIntegrationTest;
import org.junit.jupiter.api.Test;

class DeleteTransactionTests extends BaseIntegrationTest {

	/** 正常系: 削除後に GET で 404 */
	@Test
	void testDeleteTransactionSuccess() throws Exception {
		int txnId = 1;
		mockMvc.perform(delete("/api/transactions/{id}", txnId))
			.andExpect(status().isNoContent());

		mockMvc.perform(get("/api/transactions/{id}", txnId))
			.andExpect(status().isNotFound());
	}

	/** 異常系: 存在しない ID */
	@Test
	void testDeleteTransactionNotFound() throws Exception {
		int nonExistent = 9999;
		mockMvc.perform(delete("/api/transactions/{id}", nonExistent))
			.andExpect(status().isNotFound());
	}
}
