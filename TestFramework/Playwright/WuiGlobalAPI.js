class WuiPage {
	constructor(page, test, expect) {
		this.__page = page;
		this.__test = test;
		this.__expect = expect;
	}

	async goto(url) {
		await this.__page.goto(url);
	}

	async clickButton(selector) {
		await this.__page.click(selector);
	}

	async openModal(selector) {
		await this.__page.click(selector);
		await this.waitFor("Timeout", 1000);
	}

	async selectDropDownOption(id, option) {	
		await this.__page.click(`label[for="${id.replace("#", "")}"]`);

		await this.__page.click(option, {trial: true});
	}

	async toggleSwitch(action, id) {
		switch (action) {
		case "on":
			await this.__page.check(`label[for="${id.replace("#", "")}"]`);
			break;
		case "off":
			await this.__page.uncheck(`label[for="${id.replace("#", "")}"]`);
			break;
		}
	}

	async login() {
		await this.__page.goto("/");
		await this.waitFor("Selector", "#main-contents");
		const alreadyLogin = await this.__page.locator("#globalnavSystem").isVisible();
		if (!alreadyLogin) {
			await this.__page.click("a.xux-loginout");	
			await this.__page.fill("#loginName", "11111");
			await this.__page.fill("#loginPsw", "x-admin");
			await this.__page.click("#loginButton");
			await this.__page.click("#securityAlertConfirmKoDefault");
			await this.__page.click("#securityAlertConfirmSnmpDefault");	
		}
	}

	async fill(value, inSelector) {
		await this.__page.fill(inSelector, value);
	} 

	async waitFor(option, parameter, optionSetting) {
		// Do something with the settler option. 
		await this.__page[`waitFor${option}`](parameter, optionSetting);
	}

	async screenShotDiffWith(snapName) {
		this.__expect(await this.__page.screenshot()).toMatchSnapshot(snapName);
	}
}

module.exports = WuiPage;