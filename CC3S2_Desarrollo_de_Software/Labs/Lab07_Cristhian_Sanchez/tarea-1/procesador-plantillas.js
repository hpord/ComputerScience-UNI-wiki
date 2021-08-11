class TemplateProcessor {
	constructor(template) {
		this.template = template;
	}

	fillIn(dictionary) {
		/* var temp = this.template;
        for (var key in dictionary) {
            var re = new RegExp('\\{\\{' + key + '\\}\\}');
            temp = temp.replace(re, dictionary[key]);
        }
        temp = temp.replace(new RegExp('\\{\\{\\w+\\}\\}', "g"), "");
        return temp; */
		var res = this.template;
		var re = /{{[^{]*}}/g;
		var match = this.template.match(re);
		var pre, key, after;
		for (var i = 0; i < match.length; i++) {
			pre = match[i];
			key = pre.replace('{{', '');
			key = key.replace('}}', '');
			after = dictionary[key] || '';

			res = res.replace(pre, after);
		}
		return res;
	}
}
exports.TemplateProcessor = TemplateProcessor;
