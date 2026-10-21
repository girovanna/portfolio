# -*- coding: utf-8 -*-
"""Fusiona el about viejo (tarjetas) con el nuevo y elimina la sección duplicada."""
p = r"C:\Users\Anna\portfolio-pages\index.html"
s = open(p, encoding="utf-8").read()

# 1) enriquecer mi about con lo bueno del viejo
viejo2 = "<p class=\"about-lead\">Mi objetivo con cada vídeo es que <strong>parezca la recomendación de una amiga, no un anuncio</strong>. Por eso funciona en paid ads: quien lo ve no siente que le están vendiendo.</p>"
nuevo2 = "<p class=\"about-lead\">Mi objetivo con cada vídeo es que <strong>parezca la recomendación de una amiga, no un anuncio</strong>, sin sobreactuación ni filtros que disfracen el producto. Por eso funciona en paid ads: quien lo ve no siente que le están vendiendo.</p>"

viejo3 = "<p class=\"about-lead\">Trabajo con <strong>brief claro y entrega en 3-5 días</strong>. Grabo en <strong>español, inglés y catalán</strong>, así que el mismo contenido puede servir para varios mercados sin duplicar producción.</p>"
nuevo3 = "<p class=\"about-lead\">Trabajo con <strong>brief claro y entrega en 3-5 días</strong>. Todo el material — vídeo completo, raw y fotos — se entrega <strong>etiquetado y organizado</strong>, listo para que la marca lo use sin esfuerzo. Grabo en <strong>español, inglés y catalán</strong>, así que el mismo contenido puede servir para varios mercados sin duplicar producción.</p>"

for a, b in ((viejo2, nuevo2), (viejo3, nuevo3)):
    if a in s:
        s = s.replace(a, b, 1)
        print("✅ about enriquecido")
    else:
        print("⚠️ no encontré un párrafo esperado")

# 2) eliminar la sección ABOUT duplicada
if "    <!-- ABOUT -->" in s:
    ini = s.index("    <!-- ABOUT -->")
    fin = s.index("    <!-- CTA — foto izquierda, texto derecho -->")
    s = s[:ini] + s[fin:]
    print("✅ sección ABOUT duplicada eliminada")
else:
    print("⚠️ no encuentro el bloque ABOUT duplicado")

open(p, "w", encoding="utf-8").write(s)
print("Sobre mí (párrafos) →", s.count('<h2 class="section-title">Sobre mí</h2>'))
