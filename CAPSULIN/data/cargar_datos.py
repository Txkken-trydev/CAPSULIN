import sqlite3

conexion = sqlite3.connect("medicamentos.db")
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    componentes TEXT,
    uso TEXT,
    presentacion TEXT,
    categoria TEXT,
    sintomas TEXT
)
''')

medicamentos = [
    # Analgésicos, Antipiréticos, Antiinflamatorios
    ("Fixadol", "Diclofenac Potásico", "Analgésico, Antipirético, Antiinflamatorio", "20 cápsulas de 50 mg", "Analgésico", "dolor, fiebre, inflamación"),
    ("Fixadol", "Diclofenac Potásico", "Analgésico, Antipirético, Antiinflamatorio", "20 cápsulas de 100 mg", "Analgésico", "dolor, fiebre, inflamación"),
    ("Acetaminofén", "Acetaminofén", "Analgésico, Antipirético", "100 tabletas de 500 mg", "Analgésico", "dolor, fiebre"),
    ("Ácido Mefenámico", "Ácido Mefenámico", "Analgésico, Antipirético", "100 tabletas de 500 mg", "Analgésico", "dolor, fiebre"),
    ("Celecoxib", "Celecoxib", "Analgésico, Antipirético", "100 tabletas de 200 mg", "Analgésico", "dolor, fiebre"),
    ("Diclofenac Potásico", "Diclofenac Potásico", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas recubiertas de 100 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Diclofenac Potásico", "Diclofenac Potásico", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas recubiertas de 50 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Diclofenac Potásico", "Diclofenac Potásico", "Analgésico, Antipirético, Antiinflamatorio", "100 cápsulas con micro-pellets de 100 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Diclofenac Potásico", "Diclofenac Potásico", "Analgésico, Antipirético, Antiinflamatorio", "10 ampollas de 75 mg/3 mL", "AINE", "dolor, fiebre, inflamación"),
    ("Diclofenac Sódico", "Diclofenac Sódico", "Analgésico, Antipirético, Antiinflamatorio", "10 ampollas de 75 mg/3 mL", "AINE", "dolor, fiebre, inflamación"),
    ("Diclofenac Sódico", "Diclofenac Sódico", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas recubiertas de 50 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Dipirona", "Dipirona", "Analgésico, Antipirético", "50 ampollas de 1g/2 mL", "Analgésico", "dolor, fiebre"),
    ("Ibuprofeno", "Ibuprofeno", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas recubiertas de 400 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Ibuprofeno", "Ibuprofeno", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas recubiertas de 600 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Ibuprofeno", "Ibuprofeno", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas recubiertas de 800 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Ibuprofeno", "Ibuprofeno", "Analgésico, Antipirético, Antiinflamatorio", "Suspensión oral 60 mL de 100 mg/5 mL", "AINE", "dolor, fiebre, inflamación"),
    ("Ibuprofeno + Tiocolchicósido", "Ibuprofeno, Tiocolchicósido", "Analgésico, Antiinflamatorio, Relajante Muscular", "100 tabletas recubiertas de 600 mg + 4 mg", "AINE", "dolor, fiebre, inflamación, contractura"),
    ("Ketoprofeno", "Ketoprofeno", "Analgésico, Antipirético, Antiinflamatorio", "20 tabletas de 100 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Ketoprofeno", "Ketoprofeno", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas de 100 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Ketoprofeno", "Ketoprofeno", "Analgésico, Antipirético, Antiinflamatorio", "10 ampollas de 100 mg/2 mL", "AINE", "dolor, fiebre, inflamación"),
    ("Ketorolaco", "Ketorolaco", "Analgésico, Antipirético, Antiinflamatorio", "10 tabletas recubiertas de 20 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Meloxicam", "Meloxicam", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas de 15 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Naproxeno", "Naproxeno", "Analgésico, Antipirético, Antiinflamatorio", "100 tabletas de 500 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Paracetamol", "Paracetamol", "Analgésico, Antipirético", "100 tabletas recubiertas de 500 mg", "Analgésico", "dolor, fiebre"),
    ("Piroxicam", "Piroxicam", "Analgésico, Antipirético, Antiinflamatorio", "100 cápsulas de 20 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Deflazacort", "Deflazacort", "Corticosteroide, Antiinflamatorio, Inmunosupresor", "20 tabletas recubiertas de 6 mg", "Corticosteroide", "inflamación, inmunosupresión"),
    ("Deflazacort", "Deflazacort", "Corticosteroide, Antiinflamatorio, Inmunosupresor", "100 tabletas recubiertas de 6 mg", "Corticosteroide", "inflamación, inmunosupresión"),
    ("Tiocolchicósido", "Tiocolchicósido", "Analgésico, Antipirético, Antiinflamatorio", "5 ampollas de 4 mg/2 mL", "AINE", "dolor, fiebre, inflamación"),
    ("Tiocolchicósido", "Tiocolchicósido", "Analgésico, Antipirético, Antiinflamatorio", "10 tabletas de 4 mg", "AINE", "dolor, fiebre, inflamación"),
    ("Laflunomida", "Laflunomida", "Antirreumático", "30 tabletas recubiertas de 20 mg", "Antirreumático", "artritis"),
    ("Fixadol Gel", "Diclofenac Sódico", "Analgésico, Antiinflamatorio", "Gel 1%", "Dermatológico", "dolor, inflamación"),
    ("Fixadol Suspensión Oral", "Diclofenac Ácido Libre", "Analgésico, Antiinflamatorio", "Suspensión oral 1.8 mg/1mL", "Pediátrico", "dolor, inflamación"),
    ("Acetaminofén Jarabe", "Acetaminofén", "Analgésico, Antipirético", "Jarabe 120 mg/5 mL, 60 mL", "Analgésico", "dolor, fiebre"),

    # Antigripal
    ("Fin-Al-Grip", "Paracetamol, Cetirizina, Fenilefrina", "Antigripal", "10 Tabletas Recubiertas de 500 mg/5 mg/10 mg", "Antigripal", "congestión nasal, estornudos, dolor de cabeza, fiebre"),
    ("Fin-Al-Grip Forte", "Paracetamol, Fenilefrina, Cetirizina, Dextrometorfano", "Antigripal", "10 Tabletas Recubiertas de 500 mg/10 mg/5 mg/15 mg", "Antigripal", "congestión nasal, estornudos, dolor de cabeza, fiebre, tos"),
    ("Fin-Al-Grip Día", "Paracetamol, Fenilefrina, Dextrometorfano", "Antigripal", "Tabletas", "Antigripal", "congestión nasal, dolor de cabeza, fiebre, tos"),
    ("Fin-Al-Grip Noche", "Paracetamol, Fenilefrina, Feniramina", "Antigripal", "Tabletas", "Antigripal", "congestión nasal, dolor de cabeza, fiebre"),

    # Sistema Respiratorio
    ("Amoxol", "Ambroxol Clorhidrato", "Expectorante", "20 tabletas de 30 mg", "Respiratorio", "tos, congestión"),
    ("Bromuro de Ipratropio", "Bromuro de Ipratropio", "Broncodilatador", "Suspensión Aerosol para inhalar 200 Dosis de 20 mcg/dosis", "Respiratorio", "asma, broncoespasmo"),
    ("Budesonida", "Budesonida", "Corticosteroide, Antiinflamatorio", "Suspensión Aerosol para inhalar 200 Dosis de 200 mcg/dosis", "Respiratorio", "inflamación vías respiratorias, asma"),
    ("Budesonida", "Budesonida", "Corticosteroide, Antiinflamatorio", "Suspensión para Inhalar 10 mL de 1 mg/5 mL", "Respiratorio", "inflamación vías respiratorias, asma"),
    ("Ambroxol Loratadina", "Ambroxol, Loratadina", "Expectorante, Antialérgico", "Jarabe 120 mL de 30 mg+5 mg/5 mL", "Respiratorio", "tos, alergia"),
    ("Ambroxol", "Ambroxol", "Expectorante", "Jarabe 120 mL de 15 mg/5 mL", "Respiratorio", "tos"),
    ("Ambroxol", "Ambroxol", "Expectorante", "Jarabe 120 mL de 30 mg/5 mL", "Respiratorio", "tos"),
    ("Bromhexina", "Bromhexina", "Antitusígeno", "Jarabe 120 mL de 4 mg/5 mL", "Respiratorio", "tos"),
    ("Bromhexina", "Bromhexina", "Antitusígeno", "Jarabe 120 mL de 8 mg/5 mL", "Respiratorio", "tos"),
    ("Cetirizina", "Cetirizina", "Antialérgico", "100 Tabletas Recubiertas de 10 mg", "Respiratorio", "alergia"),
    ("Cetirizina", "Cetirizina", "Antialérgico", "Jarabe 60 mL de 5 mg/5 mL", "Respiratorio", "alergia"),
    ("Clorfeniramina", "Clorfeniramina", "Antialérgico", "10 Ampollas de 10 mg/1 mL", "Respiratorio", "alergia"),
    ("Clorfeniramina", "Clorfeniramina", "Antialérgico", "100 Tabletas de 4 mg", "Respiratorio", "alergia"),
    ("Desloratadina", "Desloratadina", "Antialérgico", "Jarabe 60 mL de 0.5 mg/1 mL", "Respiratorio", "alergia"),
    ("Desloratadina", "Desloratadina", "Antialérgico", "100 Tabletas Recubiertas de 5 mg", "Respiratorio", "alergia"),
    ("Desloratadina", "Desloratadina", "Antialérgico", "20 Tabletas Recubiertas de 5 mg", "Respiratorio", "alergia"),
    ("Desloratadina Montelukast", "Desloratadina, Montelukast", "Antialérgico, Corticosteroide", "30 Tabletas Recubiertas de 5 mg/10 mg", "Respiratorio", "asma, alergia"),
    ("Dexametasona", "Dexametasona", "Corticosteroide, Antiinflamatorio, Antialérgico", "50 Ampollas de 8 mg/2 mL", "Respiratorio", "inflamación, alergia"),
    ("Loratadina", "Loratadina", "Antialérgico", "100 Tabletas de 10 mg", "Respiratorio", "alergia"),
    ("Loratadina", "Loratadina", "Antialérgico", "Jarabe 60 mL de 5 mg/5 mL", "Respiratorio", "alergia"),
    ("Montelukast", "Montelukast", "Antialérgico, Antiinflamatorio", "100 Tabletas Recubiertas de 10 mg", "Respiratorio", "asma, alergia"),
    ("Prednisolona", "Prednisolona", "Corticosteroide, Antialérgico, Antiinflamatorio", "100 Tabletas de 5 mg", "Respiratorio", "alergia, inflamación"),
    ("Salbutamol", "Salbutamol", "Corticosteroide, Antiinflamatorio", "Solución para inhalar 15 mL de 5 mg/mL", "Respiratorio", "asma, inflamación vías respiratorias"),
    ("Salbutamol", "Salbutamol", "Corticosteroide, Antiinflamatorio", "Suspensión Aerosol para inhalar 200 Dosis de 100 mcg/dosis", "Respiratorio", "asma, inflamación vías respiratorias"),
    ("Betametona", "Betametona", "Corticosteroide, Antiinflamatorio, Antialérgico", "10 Ampollas de 4 mg/1 mL", "Respiratorio", "inflamación, alergia"),

    # Antimicóticos
    ("Itraconazol", "Itraconazol", "Antimicótico", "100 Cápsulas de 100 mg", "Antimicótico", "infección por hongos"),
    ("Fluconazol", "Fluconazol", "Antimicótico", "Solución Inyectable Intravenosa 100 mL de 200 mg/100 mL", "Antimicótico", "infección por hongos"),
    ("Fluconazol", "Fluconazol", "Antimicótico", "4 Tabletas Recubiertas de 200 mg", "Antimicótico", "infección por hongos"),
    ("Fluconazol", "Fluconazol", "Antimicótico", "1 Tableta Recubierta de 150 mg", "Antimicótico", "infección por hongos"),

    # Antivirales
    ("Aciclovir", "Aciclovir", "Antiviral", "100 Tabletas de 200 mg", "Antiviral", "herpes simple, varicela zóster"),
    ("Aciclovir", "Aciclovir", "Antiviral", "100 Tabletas de 400 mg", "Antiviral", "herpes simple, varicela zóster"),
    ("Valacicloir", "Valacicloir", "Antiviral", "10 Tabletas Recubiertas de 500 mg", "Antiviral", "herpes, citomegalovirus, dolor, picazón, calentura"),

    # Hospitalario
    ("Haloperidol", "Haloperidol", "Antipsicótico", "10 Ampollas de 5 mg/1 mL", "Hospitalario", "esquizofrenia, bipolaridad, psicosis"),
    ("Oxitocina", "Oxitocina", "Inductor de parto", "10 Ampollas de 10 U.I/1 mL", "Hospitalario", "inducción al parto, contracciones"),

    # Vitaminas
    ("Hierro Sacaroso", "Hierro Sacaroso", "Antianémico", "10 Ampollas de 100 mg/5 mL", "Vitamina", "anemia"),
    ("Ácido Fólico", "Ácido Fólico", "Antianémico, Prenatal", "10 Ampollas de 10 mg/1 mL", "Vitamina", "anemia, desarrollo sistema nervioso"),
    ("Ácido Fólico", "Ácido Fólico", "Antianémico, Prenatal", "100 Tabletas Recubiertas de 5 mg", "Vitamina", "anemia, desarrollo sistema nervioso"),
    ("Complejo Vitamínico B", "Complejo Vitamínico B", "Vitamina, Antianémico, Energizante", "100 Tabletas Recubiertas", "Vitamina", "anemia, energía, salud piel, cabello, uñas"),
    ("Vitamina C", "Vitamina C", "Vitamina, Antioxidante", "100 Ampollas de 500 mg/5 mL", "Vitamina", "antioxidante, sistema inmunitario"),
    ("Vitamina E", "Vitamina E", "Vitamina, Antioxidante", "30 Cápsulas Blandas de 400 U.I", "Vitamina", "antioxidante"),

    # Sistema Nervioso
    ("Sertralina", "Sertralina", "Anticonvulsivante, Antiepiléptico", "100 Tabletas Recubiertas de 50 mg", "Sistema Nervioso", "convulsiones, epilepsia"),
    ("Olanzapina", "Olanzapina", "Antipsicótico, estabilizador del ánimo", "100 Tabletas Recubiertas de 5 mg", "Sistema Nervioso", "psicosis, bipolaridad"),
]

cursor.executemany('''
INSERT INTO medicamentos (nombre, componente, uso, presentacion, categoria, sintomas)
VALUES (?, ?, ?, ?, ?, ?)
''', medicamentos)

conexion.commit()
conexion.close()
print("Datos cargados correctamente.")
