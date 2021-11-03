// playwright.config.js

const config = {
	// Global playwright configuration.

	testDir: "wuiTest", // Testcase Execution directory.

	timeout: 0,  // Each test is given 1 seconds timeout.

	retries: 0, // Two retries for each test.

	reporter: [
		["list"],	
		["allure-playwright"],  
		["json", {outputFile: "../results.json"}]
	],

	use: {
		actionTimeout: 30000,	//	Timeout for each Playwright action. Defaults to 0 (no timeout).

		headless: false,

		// viewport: { width: 1280, height: 720 },

		baseURL: "https://10.87.64.122",	// https://localhost:8080
    
		locale: "ja-JP",

		ignoreHTTPSErrors: true,
    
		video: "on-first-retry",

		screenshot: "off",  // Automatic Capture Screenshot after each test.

	},

	projects: [
		{
			name: "Chromium",
			use: {
				browserName: "chromium",
			},
		},
		{
			name: "Firefox",
			use: { browserName: "firefox" },
		},

		// {
		// 	name: "WebKit",
		// 	use: { browserName: "webkit" },
		// },
	],
};

module.exports = config;