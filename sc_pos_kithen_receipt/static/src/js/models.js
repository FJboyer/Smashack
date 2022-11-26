odoo.define("sc_pos_kithen_receipt.models", function (require) {
"use strict";

	var models = require('point_of_sale.models');

	models.load_fields('res.company', ['street','street2','city','zip']);

})