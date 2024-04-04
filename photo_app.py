import tkinter as tk
from tkinter import Label  # Label を追加
from PIL import Image, ImageTk
from pathlib import Path

class StartPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()
        
         
    def create_widgets(self):
        # テキスト１
        text1_label = tk.Label(self, text="text-battle", font=("Yu Gothic", 60, 'bold'),fg='red',)
        text1_label.pack(pady=30)

        
        # スタートボタン
        start_button = tk.Button(self, text="スタート", font=("Yu Gothic", 16),\
                                 command=lambda: self.controller.show_main_page())
        start_button.pack(pady=10) 

class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='pink')
        self.master = master
        self.create_widgets()
        
       
        

    def create_widgets(self, photo_data=0,my_name='gest',enemy_name='enemy'):
        # 左側のフレームを作成
        '''
        left_frame = tk.Frame(self, bg='pink',relief='groove')
        left_frame.grid(row=0, column=0, padx=30, pady=10)

        '''
        # 中央のフレームを作成
        center_frame = tk.Frame(self,relief='groove')
        center_frame.grid(row=0,column=1,padx=20,pady=10)
        '''
        # 右側のフレームを作成
        right_frame = tk.Frame(self, bg='pink',relief='groove')
        right_frame.grid(row=0, column=3, padx=30, pady=10)
        '''
        # フォントの設定(ゴシック体に変更し、フォントをデフォルトで16に設定
        font_style = ("Yu Gothic" ,14)

        # 左側のウィジェットの作成
        # my_chara の名前とステータスの表示
        '''
        my_chara_label = tk.Label(left_frame, text=f'{my_name}\n HP:{my_hp}\n MP:{my_mp}',relief='solid',\
                                 font=font_style,width=30)
        my_chara_label.grid(row=0, column=0, pady=30)
        
        # 指示用のテキスト表示
        my_attack_label = tk.Label(left_frame, text=f'{my_name}の攻撃:', font=font_style  )
        my_attack_label.grid(row=1, column=0)

        # 攻撃内容の登録と入力欄の設置(スピンボックスの表示
        attacks = ['===','スキル攻撃','回復魔法','魔法攻撃','通常攻撃']
        self.my_attack_action = tk.StringVar(value='===')
        my_attack_action = tk.Spinbox(left_frame,width=30, textvariable=self.my_attack_action, values=attacks, relief=tk.GROOVE, borderwidth=8 )
        my_attack_action.grid(row=2, column=0)

        # ボタンの設置とボタン動作後の処理
        attack_button = tk.Button(left_frame,relief='raised', text='攻撃開始',width=30, command=self.submit)
        attack_button.grid(row=3,column=0, pady=(10,40))

        # メッセージテキスト１の作成（Label）
        my_action = tk.Label(left_frame, text=my_message1, font=font_style, relief='groove', bd=4, width=30)
        my_action.grid(row=4, column=0, pady=30)

        # メッセージテキスト２の作成（Label）
        my_action2 = tk.Label(left_frame, text=my_message2, font=font_style, relief='groove', bd=4, width=30)
        my_action2.grid(row=5, column=0, pady=30 )
        '''
        # 中央のウィジェットの作成
        # フォトウィジェットを(Label)で作成（photo_frame）
        files = [ x for x in (Path.cwd() / 'photo').iterdir()]
        windows_path = files[photo_data]
        photo_path = windows_path.as_posix()
        image_pil = Image.open(photo_path).resize((600,500))
        image_tk = ImageTk.PhotoImage(image_pil)
        photo_label = Label(center_frame, image=image_tk)
        photo_label.image = image_tk  # 画像がガベージコレクションされないようにする
        photo_label.grid(row=0, column=0, pady=10)
        # メッセージテキストを（Labelで作成(center_frame)
        vs = tk.Label(center_frame, text=f'{my_name}  VS  {enemy_name}',font=("Yu Gothic", 12, "bold"),width=30, relief='solid',bd=4)
        vs.grid(row=1, column=0, pady=10)
        '''
        # 右側のウィジェットを作成
        # Labelで敵のパラメータ（？？？）で表示
        enemy_label = tk.Label(right_frame, text= f'{enemy_name}\n HP:???\n Mp:???',font=font_style, width=30, relief='solid')
        enemy_label.grid(row=0, column=0, pady=60)

        # メッセージテキススト３を表示
        enemy_action = tk.Label(right_frame, text=enemy_message1, font=font_style, relief='groove', bd=4, width=30)
        enemy_action.grid(row=1, column=0, pady=30)

        # メッセージテキスト４を表示（Label）
        enemy_action2 = tk.Label(right_frame, text=enemy_message2, font=font_style, relief='groove', bd=4 , width=30)
        enemy_action2.grid(row=2, column=0, pady=30)

        # 戦闘結果メッセージをlabelで表示
        result_message = tk.Label(right_frame, text=result_message, font=("Yu Gothic",15), relief='solid', bd=4,width=20, fg='red')
        result_message.grid(row=3, column=0, pady=60)

    # ボタンが押されたときの処理
    def submit(self):
        print('tkinter:',self.my_attack_action.get())     
        attack_result = self.my_attack_action.get()
        return attack_result
        
     '''   

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600") 
        self.title("battle-game")
       # self.show_start_page()
        self.show_main_page()
       

    def show_main_page(self):
        # メインページの表示
       
        self.main_page = MainPage(self)
        #self.start_page.pack_forget()  # スタートページを非表示にする
        self.main_page.pack()
      
        
if __name__ == "__main__":
    app = Application()
    app.mainloop()
