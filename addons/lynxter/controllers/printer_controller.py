from odoo import http
class Printers(http.Controller):
    @http.route("/lynxter/allprinters", type='http', auth='public', website=True)
    def list(self, **kwargs) :
        Printer=http.request.env["lynxter.printer"]
        printers=Printer.search([])
        return http.request.render("lynxter.printer_list_template", {"printers":printers})
  