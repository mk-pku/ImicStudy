package com.example.api;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collections;
import java.util.Map;

/**
 * シンプルな Hello World 用 RestController。
 * GET /hello にアクセスすると JSON 形式でメッセージを返す。
 */
@RestController
public class HelloController {

	@GetMapping("/hello")
	public Map<String, String> hello() {
		// JSON: {"message":"Hello, World!"}
		return Collections.singletonMap("message", "Helloaaa, World!");
	}
}
