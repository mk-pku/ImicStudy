package com.example.api.controller;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import com.example.api.BaseIntegrationTest;
import org.junit.jupiter.api.Test;

class GetListTransactionTests extends BaseIntegrationTest {

	/** 正常系: 全件取得 */
	@Test
	void testGetListTransactionSuccess() throws Exception {
		mockMvc.perform(get("/api/transactions"))
			.andExpect(status().isOk())
			.andExpect(jsonPath("$").isArray());
	}
}
