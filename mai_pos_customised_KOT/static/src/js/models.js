odoo.define('mai_pos_customised_KOT.models', function(require) {
	"use strict";

	var models = require('point_of_sale.models');
	var core = require('web.core');
	var rpc = require('web.rpc');
	var utils = require('web.utils');
	var _t = core._t;
	var Printer = require('point_of_sale.Printer').Printer;
	var QWeb = core.qweb;
	var field_utils = require('web.field_utils');

	var _super_order = models.Order.prototype;
	models.Order = models.Order.extend({
		
		printChanges: async function(){
			var printers = this.pos.printers;
			let isPrintSuccessful = true;
			let client = this.get_client().name;
			// let cashier = this.pos.get_cashier().name;
			let cashier = this.pos.config.name;
			for(var i = 0; i < printers.length; i++){
				var changes = this.computeChanges(printers[i].config.product_categories_ids);
				changes['client'] = client;
				changes['cashier'] = cashier;
				changes['date']  = field_utils.format.datetime( moment(new Date()), {}, {timezone: false});
				if ( changes['new'].length > 0 || changes['cancelled'].length > 0){
					var receipt = QWeb.render('OrderChangeReceipt',{changes:changes, widget:this});
					const result = await printers[i].print_receipt(receipt);
					if (!result.successful) {
					    isPrintSuccessful = false;
					}
				}

			}
			return isPrintSuccessful;
		},

	});
	
 
});
