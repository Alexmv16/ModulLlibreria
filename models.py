from odoo import models, fields

class Categoria(models.Model):
    _name = 'biblioteca.categoria'
    _description = 'Categoría de libros'

    name = fields.Char(string='Nombre', required=True, help='Introduïx el nom de la categoria')
    descripcion = fields.Text(string='Descripción')

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string='Nombre', required=True)
    precio = fields.Float(string='Preu')
    exemplares = fields.Integer(string='Exemplares')
    rotura_estoc = fields.Boolean(string='Rotura Estoc', compute='_compute_rotura_estoc', store=True)
    data = fields.Date(string='Data')
    segonama = fields.Boolean(string='Segonama')
    estat = fields.Selection([
        ('bo', 'Bo'),
        ('regular', 'Regular'),
        ('dolent', 'Dolent'),
    ], string='Estat', default='bo')

    @staticmethod
    def _compute_rotura_estoc(self):
        for record in self:
            record.rotura_estoc = record.exemplares < 10
