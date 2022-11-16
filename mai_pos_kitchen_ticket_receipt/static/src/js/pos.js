odoo.define('mai_pos_kitchen_ticket_receipt.order', function (require) {
"use strict";
    var core = require('web.core');
    var screens = require('point_of_sale.screens');
    var models = require('point_of_sale.models');
    var QWeb = core.qweb;
    var _t = core._t;

    var OrderSuper = models.Order;
    models.Order = models.Order.extend({
            export_kitchen_receipt: function(){
                var order_lines = this.get_orderlines();
                var data = [];
                for(var i=0;i<order_lines.length;i++){
                    if(i==0){
                        data.push({'order_line':order_lines[i],'line_data':[]})
                    }
                    else{
                        data[data.length-1]['line_data'].push(order_lines[i])
                    }
                }
            return data;
        }
    });

});

