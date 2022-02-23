import os
import PySimpleGUI as sg
class Organizar:
    def __init__(self):
        self.caminho = ''
    def Tela(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Caminho desejado:'),sg.Input(),sg.FolderBrowse(key='caminho')],
            [sg.Button('organizar',key='go')]
        ]
        return sg.Window('Organizador de pastas',layout=layout,element_justification='center',finalize=True)


    def ChamarTela(self):
        self.janela = self.Tela()
        while True:
            event , values = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'go':
                self.caminho = values['caminho']
                break


    def PercorrerPasta(self):

        for arquivo in os.listdir(self.caminho):
            c = 1
            if '.png' in arquivo or '.jpg' in arquivo or '.jpeg' in arquivo or '.ico' in arquivo or '.jfif' in arquivo:
                if not os.path.isdir(f'{self.caminho}\Imagens'):
                    os.mkdir(f'{self.caminho}\Imagens')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Imagens/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Imagens/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break

            elif '.exe' in arquivo or '.jar' in arquivo:
                if not os.path.isdir(f'{self.caminho}\Executaveis'):
                    os.mkdir(f'{self.caminho}\Executaveis')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Executaveis/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Executaveis/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.pdf' in arquivo:
                if not os.path.isdir(f'{self.caminho}\PDFs'):
                    os.mkdir(f'{self.caminho}\PDFs')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/PDFs/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/PDFs/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.rar' in arquivo or '.zip' in arquivo:
                if not os.path.isdir(f'{self.caminho}\ZIPs'):
                    os.mkdir(f'{self.caminho}\ZIPs')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/ZIPs/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/ZIPs/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.docx' in arquivo or '.doc' in arquivo:
                if not os.path.isdir(f'{self.caminho}\Documentos'):
                    os.mkdir(f'{self.caminho}\Documentos')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Documentos/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Documentos/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.mp3' in arquivo:
                if not os.path.isdir(f'{self.caminho}\Musicas'):
                    os.mkdir(f'{self.caminho}\Musicas')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Musicas/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Musicas/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.mp4' in arquivo or '.sfk' in arquivo:
                if not os.path.isdir(f'{self.caminho}\Videos'):
                    os.mkdir(f'{self.caminho}\Videos')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Videos/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Videos/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.txt' in arquivo or '.log' in arquivo:
                if not os.path.isdir(f'{self.caminho}\Textos'):
                    os.mkdir(f'{self.caminho}\Textos')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Textos/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Textos/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.gif' in arquivo:
                if not os.path.isdir(f'{self.caminho}\GIFs'):
                    os.mkdir(f'{self.caminho}\GIFs')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/GIFs/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/GIFs/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.torrent' in arquivo:
                if not os.path.isdir(f'{self.caminho}\TORRENTs'):
                    os.mkdir(f'{self.caminho}\TORRENTs')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/TORRENTs/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/TORRENTs/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif '.xlsx' in arquivo:
                if not os.path.isdir(f'{self.caminho}\Planilhas'):
                    os.mkdir(f'{self.caminho}\Planilhas')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Planilhas/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/Planilhas/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break
            elif arquivo != 'OutrasCoisas' and arquivo != 'Imagens' and arquivo != 'Executaveis' and arquivo != 'PDFs' and arquivo != 'ZIPs' and arquivo != 'Documentos' and arquivo != 'Musicas' and arquivo != 'Videos' and arquivo != 'Textos' and arquivo != 'GIFs' and arquivo != 'TORRENTs' and arquivo != 'Planilhas':
                if not os.path.isdir(f'{self.caminho}\OutrasCoisas'):
                    os.mkdir(f'{self.caminho}\OutrasCoisas')
                while True:
                    try:
                        os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/OutrasCoisas/{arquivo}')
                    except FileExistsError:
                        while True:
                            try:
                                os.rename(f'{self.caminho}/{arquivo}', f'{self.caminho}/OutrasCoisas/{c}_{arquivo}')
                            except:
                                c += 1
                            else:
                                break
                    else:
                        break


    def Organizador(self):
        self.ChamarTela()
        self.janela.close()
        while True:
            try:
                self.PercorrerPasta()
            except FileNotFoundError:
                print('erro de não encontrar o arquivo , repetindo o processo!')
            else:
                break
        sg.popup('Pasta Organizada Com Sucesso!')


app = Organizar()
app.Organizador()