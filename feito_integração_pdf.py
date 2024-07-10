import streamlit as st
import io
import pypdf as pyf



st.title('Juntado PDFs')




up_pdf= st.file_uploader(
    label="Escolha um arquivo PDF", 
    type="pdf", 
    accept_multiple_files=True
)


def juntado(pdfs):
    agrupando_pdf= pyf.PdfWriter()
    for pdf in pdfs:
        agrupando_pdf.append(pdf)            
    return agrupando_pdf

def gerar_pdf_agrupado():
    if up_pdf:
        novo_pdf = juntado(up_pdf)
        output = io.BytesIO()
        novo_pdf.write(output)
        output.seek(0)
        return output
    
    
def download_button():
    if up_pdf:
        new_pdf=gerar_pdf_agrupado()
        st.download_button(
            label='Baixar arquivos mesclados',
            data=new_pdf,
            file_name='PDF mesclado.pdf',
            mime='application/pdf'
        )
        
        
        
download_button()