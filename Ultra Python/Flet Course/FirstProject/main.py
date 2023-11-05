from flet import (UserControl,Page,CrossAxisAlignment,MainAxisAlignment,Container,RadialGradient,Alignment,border,ClipBehavior,Column,CrossAxisAlignment,app,padding)

class AppTitle(UserControl):
    def __init__(self):
        super().__init__()
    
    def InputContainer(self,width:int):
        return Container(
            width=width,
            height=40,
            bgcolor="white10"
        )
    def build(self):
        return Container(
            padding=padding.only(top=20, left=15, right=15),
            content=Column(
                
            )
        )
def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER,
    page.vertical_alignment = MainAxisAlignment.CENTER,
    page.bgcolor = 'white10'
    
    _main_ = Container(
        width=290,
        height=600,
        gradient=RadialGradient(
            center=Alignment(-0.5, -0.8),
            radius=3,
            colors=[
                "#33354a",
                "#2f3143",
                "#2f3143",
                "#292b3c",
                "#222331",
                "#222331",
                "#1a1a25",
                "#1a1a26",
                "#1a1a26",
                "#21222f",
                "#1d1e2a",
                "black"
            ],
        ),
        border_radius=30,
        border=border.all(width=1, color="white"),
        padding=10,
        clip_behavior=ClipBehavior.HARD_EDGE,
        content=Column(
            scroll='none',
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
            ]
        )
    )
    page.add(_main_)
    page.update()

if __name__ == "__main__":
    app(target=main)