import PyPDF2
from pathlib import Path


def pdf_para_texto(pdf_path: str):
    """Converte um PDF para TXT com o mesmo nome."""
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print(f"❌ Erro: Arquivo não encontrado: {pdf_path}")
        return

    if not pdf_path.suffix.lower() == '.pdf':
        print(f"❌ Erro: O arquivo deve ser um PDF: {pdf_path}")
        return

    txt_path = pdf_path.with_suffix('.txt')

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            texto_completo = []

            for i, pagina in enumerate(reader.pages):
                texto = pagina.extract_text()
                if texto:
                    texto_completo.append(texto)
                else:
                    texto_completo.append(f"[Página {i + 1} sem texto extraível]")

            texto_final = "\n\n".join(texto_completo)

        # Salva o arquivo .txt
        with open(txt_path, 'w', encoding='utf-8') as file:
            file.write(texto_final)

        print(f"✓ Convertido: {pdf_path.name} → {txt_path.name}")

    except Exception as e:
        print(f"❌ Erro ao processar {pdf_path.name}: {e}")


def converter_todos_pdfs(pasta: str = None):
    """Itera por todos os arquivos .pdf em assets/dataset_texto e gera os .txt correspondentes."""
    if pasta is None:
        # Resolve o caminho relativo à raiz do projeto (um nível acima de src/)
        pasta = Path(__file__).resolve().parent.parent / "assets" / "dataset_texto"
    else:
        pasta = Path(pasta)

    if not pasta.exists():
        print(f"❌ Erro: Pasta não encontrada: {pasta}")
        return

    pdfs = list(pasta.rglob("*.pdf"))

    if not pdfs:
        print(f"⚠️ Nenhum arquivo .pdf encontrado em: {pasta}")
        return

    print(f"📂 Encontrados {len(pdfs)} arquivo(s) PDF em: {pasta}\n")
    for pdf in pdfs:
        pdf_para_texto(str(pdf))
    print("\n✅ Conversão concluída!")


# ===================== USO =====================
if __name__ == "__main__":
    converter_todos_pdfs()
