
  def test_balances_positivos_devuelve_todos_los_balances_si_todos_tienen_ganancia_mayor_a_cero(self):
	  self.assertEqual(balances_positivos([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": 8 }]), [{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": 8 }])

  def test_balances_positivos_excluye_a_los_balances_con_ganancia_cero(self):
	  self.assertEqual(balances_positivos([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": 0 }]), [{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }])

  def test_balances_positivos_excluye_a_los_balances_con_ganancia_negativa(self):
	  self.assertEqual(balances_positivos([{ "mes": "julio", "ganancia": 12 }, { "mes": "agosto", "ganancia": -2 }]), [{ "mes": "julio", "ganancia": 12 }])
 
  def test_balances_positivos_devuelve_la_lista_vacia_si_todos_los_balances_tienen_ganancia_de_cero_o_menos(self):
	  self.assertEqual(balances_positivos([{ "mes": "agosto", "ganancia": -12 }, { "mes": "septiembre", "ganancia": 0 }]), [])