from manim.opengl import *

from custom_manim_utils.custom_mobs import *
import manim.utils.space_ops
from manim import *

import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
# from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_mobs import *
from custom_manim_utils.custom_mobs import *
from manim_physics import *
from manim_gearbox import *
from pathlib import Path

from pprint import pprint

config.frame_width = 16
config.frame_height = 9


# background_color = W02


class final(Scene):
    def construct(self):
        self.add(NumberPlane())
        # lec1_s1.construct(self)


class working4(MovingCameraScene):
    def construct(self):
        #     self.add(NumberPlane())
        self.camera.frame.save_state()
        #     self.add(NumberPlane())
        self.camera.frame.save_state()

        speak(self, title='Scene2', txt=

        '가격이라는 것에 대해 정확하게 정의하고 가겠습니다#1'
        '가격은 경제,비즈니스면에서 물건,용역,자산의 금전적 수적가치를 따지는 것으로, 한 제품 및 서비스의 가격이란 소비자가 그 제품이나 서비스를 한 단위로 구매하기 위해 지불해야 하는 화폐의 양을 말한다#1'
        '비티씨 테더 페어에서 38000테더라고 적혀있다면 있다면 우리는 비티씨의 가격이 얼마라고 얘기합니까#1'
        '38000달러라고 부릅니다. 그러나 이는 엄밀하게 보면 틀린 표현입니다#1'
        '비티씨의 가격은 38000테더입니다. 테더와 달러는 다른 것입니다 #1'
        '달러는 달러 그자체이고 테더는 이 달러를 담보로 발행했기에 테더 회사가 지급불능이 된다면 테더는 디지털 쓰레기가 됩니다#1'
        '달러를 옹호하는 건 아닙니다. 미국정부가 망하면 달러는 종이 쓰레기가 됩니다#1'
        '그리고 국민이 없다면 정부는 존재할 수 없습니다#1'
        '테더는 실제로 거래해보면 보통 0.999에서 1.001 달러 사이를 움직이며 거래됩니다#1'
        '금본위제 시절에 달러가 금하고 바꿀 수 있는 종이였지 금이 아니듯 테더는 달러가 아니고 가치가 미세하지만 어쨌든 변동하는 자산입니다#1'
        '지금까지의 얘기는 무의식적으로 달러와 테더가 같다고 여겨지는 생각을 없애기 위함이고 이것은 나중에 논스테이블 페어를 이해하는데 도움이 됩니다#1'

        '가격은 어떻게 움직일까요#1'
        '우리가 배우기로는 수요와 공급이 교차하는 지점에서 결정된다고 배웁니다#1'
        '그러나 거래소에서의 가격은 그 말보다는 인내심이 더 부족한 쪽에 의해 결정된다고 하는게 이해하기 쉬울겁니다#1'
        '누구나 더 높은 가격에 팔고 더 낮은 가격에 사고 싶기 때문에 호가창에는 지정가 주문들이 쌓이기 시작합니다#1'
        '그렇게 지정가 주문들이 현재가 위 아래로 계속 쌓이기만 하면 가격은 움직이지 않습니다 #1'
        '실제로 호가창에 100달러와 101달러가 맞닿아 있고 아무도 시장가 주문을 넣지 않으면 가격은 마지막 거래가 100원에서 매수였으면 100원, 101원에서 매도였으면 101원에 정지해있습니다#1'
        '그러다가 누군가 기다림을 참지 못하고 시장가로 구매를 하면 호가창에 쌓여있던 물량이 시장가로 소화되면서 가격은 움직입니다 #1'
        '잘 생각해보면 모든 사람이 지정가 주문만 넣으면 아무 일도 일어나지 않고 모두 기다리기만 합니다#1'

              , keep_pitch=True, update=1, speed=1.4)
        # TODO 3.117 secs가격이라는 것에 대해 정확하게 정의하고 가겠습니다
        # TODO 0:00:00.000  ~  0:00:03.117
        # TODO 1.0secs pause
        # TODO 0:00:03.117  ~  0:00:04.117

        # TODO 13.845 secs가격은 경제,비즈니스면에서 물건,용역,자산의 금전적 수적가치를 따지는 것으로,
        #  한 제품 및 서비스의 가격이란 소비자가 그 제품이나 서비스를 한 단위로 구매하기 위해 지불해야하는 화폐의양을말한다
        # TODO 0:00:04.117  ~  0:00:17.962
        # TODO 1.0secs pause
        # TODO 0:00:17.962  ~  0:00:18.962
        price = Tex('Price').scale(2)

        self.play(Create(price), run_time=3.117)

        price_text = Tex(
            r'A price is the (usually not negative) quantity of payment \\'
            r'or compensation given by one party to another\\in return for goods or services.').next_to(
            price, D)
        self.play(Create(price_text), run_time=10)
        self.wait(3)

        self.play(Uncreate(price),
                  Uncreate(price_text), run_time=2.845)

        # TODO 6.584 secs비티씨 테더 페어에서 38000테더라고 적혀있다면 있다면 우리는 비티씨의 가격이 얼마라고 얘기합니까
        # TODO 0:00:18.962  ~  0:00:25.546
        # TODO 1.0secs pause
        # TODO 0:00:25.546  ~  0:00:26.546

        # TODO 4.591 secs38000달러라고 부릅니다. 그러나 이는 엄밀하게 보면 틀린 표현입니다
        # TODO 0:00:26.546  ~  0:00:31.137
        # TODO 1.0secs pause
        # TODO 0:00:31.137  ~  0:00:32.137

        # TODO 4.639 secs비티씨의 가격은 38000테더입니다. 테더와 달러는 다른 것입니다
        # TODO 0:00:32.137  ~  0:00:36.776
        # TODO 1.0secs pause
        # TODO 0:00:36.776  ~  0:00:37.776

        pair_rect = RoundedRectangle(corner_radius=0.5, height=7, width=4)
        pair_rect_text = Tex("BTCUSDT").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text)

        self.play(Create(pair),
                  run_time=2)

        curr_px_usdt = Tex('38000 USDT').move_to(pair_rect)
        curr_px = Tex('38000').move_to(pair_rect)
        curr_px_usd = Tex('38000 USD?').next_to(pair_rect, R)

        self.play(Create(curr_px_usdt),
                  run_time=2)
        self.wait(2)

        self.play(Create(curr_px_usd),
                  run_time=2)

        curr_px_usd_cross = Cross(curr_px_usd)
        self.wait(1)

        self.play(Create(curr_px_usd_cross),
                  run_time=1)

        circle_curr_px = Circle(color=GREEN, radius=1, stroke_width=25).rotate(PI / 2).move_to(curr_px_usdt)
        self.wait(2)

        usdt_1 = create_entity("A", 0.5, WHITE, "USDT", C_USDT, 2, 1, asset_text_color=WHITE, scaler=0.8)[ 1 ]
        usd_1 = create_entity("A", 0.5, WHITE, "USD", '#9DC87B', 2, 1, asset_text_color='#2A5A25', scaler=0.8)[ 1 ]
        equal = MathTex(r'\neq').scale(2)

        n_eq_form = VGroup(usd_1, equal, usdt_1).arrange(RIGHT, buff=0.5)
        # self.play(Create(n_eq_form))
        #
        #
        # not_equal= Tex(r'USD \neq USDT')
        self.play(ReplacementTransform(VGroup(pair, curr_px_usdt, curr_px_usd_cross, curr_px_usd, circle_curr_px), n_eq_form),
                  run_time=3)
        # self.wait(q)
        #
        # self.play(Uncreate(not_equal))
        #
        #
        n_eq_form = VGroup(usd_1, equal, usdt_1).arrange(RIGHT, buff=0.5).scale(2)
        # usg = LabeledDot(Tex(r'\emph{US\\Gov}',color=BLACK ), radius=1)[ 0].to_edge(D, buff=0.5)
        # us_people = LabeledDot(Tex(r'\emph{US\\People}',color=BLACK), radius=1)[ 0].to_edge(DR, buff=0.5)
        #
        # backed_by_1 = Tex('Backed by').move_to(np.array([usdt.get_x(),0,0]))
        # backed_by_2 = Tex('Backed by')
        # backed_by_3 = Tex('Backed by').move_to(np.array([usg.get_x(),0,0]))

        self.wait(2)
        self.play(Uncreate(n_eq_form),
                  run_time=1.814)

        # btc_equal_38000 = Tex('1 BTC = 38000')
        # cross = Cross(stroke_width=25).scale(3)
        # btc_equal_38000dollars = Tex('1 BTC = 38000 USD')
        # circle = Circle(color=GREEN, radius=3, stroke_width=25).rotate(PI / 2)
        # self.play(Create(btc_equal_38000))
        #
        # self.play(Create(cross))
        #
        # self.play(FadeOut(cross))
        # self.play(TransformMatchingShapes(btc_equal_38000, btc_equal_38000dollars))
        #
        # self.play(Create(circle))
        #
        # self.play(FadeOut(circle),
        #           Uncreate(btc_equal_38000dollars))
        #
        # self.wait(q)

        # TODO 7.55 secs달러는 달러 그자체이고 테더는 이 달러를 담보로 발행했기에 테더 회사가 지급불능이 된다면 테더는 디지털 쓰레기가 됩니다
        # TODO 0:00:37.776  ~  0:00:45.326
        # TODO 1.0secs pause
        # TODO 0:00:45.326  ~  0:00:46.326

        usdt = create_entity("A", 0.5, WHITE, "USDT", C_USDT, 2, 1, asset_text_color=WHITE, scaler=0.8)[ 1 ].to_edge(UL, buff=1)
        usd = create_entity("A", 0.5, WHITE, "USD", '#9DC87B', 2, 1, asset_text_color='#2A5A25', scaler=0.8)[ 1 ].to_edge(DL, buff=1)
        usg = SVGMobject('svgs/government.svg', fill_color=WHITE).scale(0.85).to_edge(D, buff=0.7)
        us_people = SVGMobject('svgs/people.svg', fill_color=WHITE).scale(0.85).to_edge(D, buff=0.7).to_edge(R, buff=1)

        usd_copy = usd.copy().move_to(ORIGIN).to_edge(U, buff=1)

        usg_copy = usg.copy().move_to(ORIGIN).to_edge(U, buff=0.5).to_edge(R, buff=1)
        us_people.move_to([ usg_copy.get_x(), us_people.get_y(), 0 ])

        backed_by_1 = Tex('Backed by').move_to(np.array([ usdt.get_x(), 0, 0 ]))
        backed_by_2 = Tex('Backed by')
        backed_by_3 = Tex('Backed by').move_to(np.array([ us_people.get_x(), 0, 0 ]))

        self.play(Create(usdt), run_time=0.5)
        self.play(Create(backed_by_1), run_time=0.5)
        self.play(Create(usd), run_time=0.5)
        self.play(TransformFromCopy(usd, usd_copy), run_time=0.5)
        self.play(Create(backed_by_2), run_time=0.5)
        self.play(Create(usg), run_time=0.5)
        self.play(TransformFromCopy(usg, usg_copy), run_time=0.5)
        self.play(Create(backed_by_3), run_time=0.5)
        self.play(Create(us_people), run_time=0.5)

        self.wait(2)

        self.play(FadeOut(VGroup(usd, backed_by_1)), run_time=0.5)
        self.wait(1)
        self.play(Uncreate(usdt), run_time=0.55)

        # TODO 4.881 secs달러를 옹호하는 건 아닙니다. 미국정부가 망하면 달러는 종이 쓰레기가 됩니다
        # TODO 0:00:46.326  ~  0:00:51.207
        # TODO 1.0secs pause
        # TODO 0:00:51.207  ~  0:00:52.207
        self.play(FadeOut(VGroup(usg, backed_by_2)),
                  run_time=1.881)
        self.wait(1.5)
        self.play(Uncreate(usd_copy),
                  run_time=1)
        self.wait(1.5)

        # TODO 3.165 secs그리고 국민이 없다면 정부는 존재할 수 없습니다
        # TODO 0:00:52.207  ~  0:00:55.372
        # TODO 1.0secs pause
        # TODO 0:00:55.372  ~  0:00:56.37
        self.play(FadeOut(VGroup(us_people, backed_by_3)),
                  run_time=1)
        self.wait(1)
        self.play(Uncreate(usg_copy),
                  run_time=1.165)
        self.wait(1)

        # TODO 5.98 secs테더는 실제로 거래해보면 보통 0.999에서 1.001 달러 사이를 움직이며 거래됩니다
        # TODO 0:00:56.372  ~  0:01:02.352
        # TODO 1.0secs pause
        # TODO 0:01:02.352  ~  0:01:03.352

        price_of_usdt = Tex(r'Price of 1 "USDT" is \\normally 1.01 \textasciitilde \  0.99 "USD"').scale(1.5)

        self.play(Create(price_of_usdt), run_time=2)
        self.wait(2)
        self.play(Uncreate(price_of_usdt), run_time=2.98)

        # TODO 8.263 secs금본위제 시절에 달러가 금하고 바꿀 수 있는 종이였지 금이 아니듯 테더는 달러가 아니고 가치가 미세하지만 어쨌든 변동하는 자산입니다
        # TODO 0:01:03.352  ~  0:01:11.615
        # TODO 1.0secs pause
        # TODO 0:01:11.615  ~  0:01:12.615

        plane = Axes(
            x_range=(0, 20),
            y_range=(0, 12),
            x_length=15,
            y_length=8,
            axis_config={"include_numbers": False,
                         'include_ticks': False},
        )
        x_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ]
        y_list = [ 5.5, 5, 6, 4, 5, 7, 5, 6, 5, 4, 5, 6, 5, 6, 7, 6, 5, 6, 7, 6.2 ]
        # plane.center()
        line_graph = plane.plot_line_graph(
            x_values=x_list,
            y_values=y_list,
            line_color=C_USDT,
            add_vertex_dots=0,
            # vertex_dot_style=dict(stroke_width=1, fill_color=PURPLE),
            stroke_width=10,
        )

        path = VMobject()
        print(plane.c2p(1, 5), plane.c2p(1, 7))

        print([ plane.c2p(x, y) for x, y in zip(x_list, y_list) ])
        path.set_points_as_corners([ plane.c2p(x, y) for x, y in zip(x_list, y_list) ])
        px = ValueTracker(1)
        px.add_updater(lambda mob: mob.become(ValueTracker(self.camera.frame.get_y())))

        label = Tex(rf'Price of USDT : {px.get_value()}')
        label.add_updater(lambda mob: mob.become(
            Tex(rf'Price of USDT\\{(1.015 - 0.985) * (self.camera.frame.get_y() - (-1 / 3)) / (1 / 3 - (-1 / 3)) + 0.985:.03f} USD').next_to(
                self.camera.frame.get_center(), UR, buff=0.5)))
        icon = SVGMobject('svgs/svg/color/usdt.svg')
        icon.add_updater(
            lambda mob: mob.become(SVGMobject('svgs/svg/color/usdt.svg').scale(0.65).next_to(self.camera.frame.get_center(), DR, buff=0.5)))

        self.play(Create(plane),
                  self.camera.frame.animate.scale(0.7).move_to(path.get_start()),
                  run_time=4)

        self.play(Create(label),
                  Create(icon), run_time=2)
        self.play(Create(line_graph),
                  MoveAlongPath(self.camera.frame, path),
                  run_time=6)

        label.clear_updaters()
        icon.clear_updaters()

        self.wait(2)

        self.play(Restore(self.camera.frame),
                  label.animate.scale(1 / 0.7).move_to([ 2, 2.5, 0 ]),
                  icon.animate.scale(1 / 0.7).move_to([ 2 - label.width / 2, 2.5, 0 ]).shift(L * 2),
                  run_time=4)

        # TODO 8.686 secs지금까지의 얘기는 무의식적으로 달러와 테더가 같다고 여겨지는 생각을 없애기 위함이고 이것은 나중에 논스테이블 페어를 이해하는데 도움이 됩니다
        # TODO 0:01:12.615  ~  0:01:21.301
        # TODO 1.0secs pause
        # TODO 0:01:21.301  ~  0:01:22.301

        self.play(Uncreate(VGroup(icon, label, line_graph, plane), run_time=0.949))

        # TODO 1.752 secs가격은 어떻게 움직일까요
        # TODO 0:00:00.000  ~  0:00:01.752
        # TODO 1.0secs pause
        # TODO 0:00:01.752  ~  0:00:02.752

        # TODO 4.578 secs우리가 배우기로는 수요와 공급이 교차하는 지점에서 결정된다고 배웁니다
        # TODO 0:00:02.752  ~  0:00:07.330
        # TODO 1.0secs pause
        # TODO 0:00:07.330  ~  0:00:08.330
        x_range = 20
        ax = Axes(x_range=[ 0, x_range, x_range / 10 ],
                  y_range=[ 0, 256, 25.6 ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": False}
                  )

        supply_val_tracker = ValueTracker(0)
        demand_val_tracker = ValueTracker(0)
        supply_graph = ax.plot(lambda x: (x - supply_val_tracker.get_value()) ** 2,
                               x_range=[ x_range * 0.2 + supply_val_tracker.get_value(), x_range * 0.8 + supply_val_tracker.get_value() ],
                               use_smoothing=False, color=BLUE)
        demand_graph = ax.plot(lambda x: (x_range - (x - demand_val_tracker.get_value())) ** 2,
                               x_range=[ x_range * 0.2 + demand_val_tracker.get_value(), x_range * 0.8 + demand_val_tracker.get_value() ],
                               use_smoothing=False, color=RED)

        supply_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: (x - supply_val_tracker.get_value()) ** 2,
                    x_range=[ x_range * 0.2 + supply_val_tracker.get_value(), x_range * 0.8 + supply_val_tracker.get_value() ],
                    use_smoothing=False, color=BLUE)))
        demand_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: (x_range - (x - demand_val_tracker.get_value())) ** 2,
                    x_range=[ x_range * 0.2 + demand_val_tracker.get_value(), x_range * 0.8 + demand_val_tracker.get_value() ],
                    use_smoothing=False, color=RED)))

        supply_graph_label = Tex('Supply').next_to(supply_graph, UR)
        supply_graph_label.add_updater(lambda label: label.become(Tex('Supply').next_to(supply_graph, UR).shift(LEFT)))
        demand_graph_label = Tex('Demand').next_to(demand_graph, DR)
        demand_graph_label.add_updater(lambda label: label.become(Tex('Demand').next_to(demand_graph, UL).shift(RIGHT)))

        labels = ax.get_axis_labels("Quantity", "Price")

        x_label = ax.get_x_axis_label(
            Tex("Quantity").scale(0.65), edge=DOWN, direction=DOWN, buff=0.5
        )
        y_label = ax.get_y_axis_label(
            Tex('Price').scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,
        )

        axis_labels = VGroup(x_label, y_label)

        supply_graph.add(supply_graph_label)
        demand_graph.add(demand_graph_label)

        # label_rect = LabeledRectangle('Government',4,5)
        self.play(Create(ax),
                  Create(supply_graph),
                  Create(demand_graph),
                  Create(axis_labels))

        self.wait(1.278)

        lines = ax.get_lines_to_point(ax.c2p(1, 3))
        lines.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
            ax.c2p((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2,
                   supply_graph.underlying_function((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2)))))
        self.add(lines)

        # horizontal_line = ax.get_horizontal_line(supply_graph)
        def reverse(t: float) -> float:
            return -t + 1

        # self.play(Create(lines[ 0 ]),
        #           Create(lines[ 1 ]))
        cross_dot = Dot(0.7).move_to(ax.c2p((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2,
                                            supply_graph.underlying_function(
                                                (20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2)))
        cross_dot_text = MathTex('Equalibrium')
        cross_dot.add_updater(lambda x: x.move_to(ax.c2p((20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2,
                                                         supply_graph.underlying_function(
                                                             (20 + supply_val_tracker.get_value() + demand_val_tracker.get_value()) / 2))))
        cross_dot_text.add_updater(lambda x: x.next_to(cross_dot, RIGHT))
        self.play(Create(cross_dot),
                  Write(cross_dot_text))

        self.play(supply_val_tracker.animate.set_value(-3))
        self.play(demand_val_tracker.animate.set_value(-3))
        self.play(demand_val_tracker.animate.set_value(3))
        self.play(supply_val_tracker.animate.set_value(3))

        supply_func = supply_graph.get_function()

        self.play(Uncreate(VGroup(supply_graph, demand_graph, ax, axis_labels, cross_dot, cross_dot_text)))

        # new_dot = Dot(0.5, color=RED).move_to(ax.c2p(5, supply_graph.underlying_function(5)))
        #
        # self.play(Create(new_dot))
        #

        # self.play(FadeOut(self.mobjects, shift=UP))

        # TODO 6.874 secs그러나 거래소에서의 가격은 그 말보다는 인내심이 더 부족한 쪽에 의해 결정된다고 하는게 이해하기 쉬울겁니다
        # TODO 0:00:08.330  ~  0:00:15.204
        # TODO 1.0secs pause
        # TODO 0:00:15.204  ~  0:00:16.204

        clock_min_angle = ValueTracker(PI / 2)
        clock_hour_angle = ValueTracker(PI / 2)
        clock_circle = Circle(color=WHITE).scale(2)
        clock_center_dot = Dot(color=WHITE)
        clock_min_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=3, buff=0,
                                 max_stroke_width_to_length_ratio=100)
        clock_hour_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                  max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=0.4)
        clock_min_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=5, buff=0,
                                                              max_stroke_width_to_length_ratio=100)))
        clock_hour_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                                               max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=0.4)))
        clock = VGroup(clock_circle, clock_center_dot, clock_min_handle, clock_hour_handle)

        self.play(Create(clock))

        self.play(AnimationGroup(AnimationGroup(clock_min_angle.animate.set_value(PI / 2 - 4 * 2 * PI),
                                                clock_hour_angle.animate.set_value(PI / 2 - 4 * 2 * PI / 12)), rate_func=linear,
                                 run_time=6))

        self.play(FadeOut(clock), run_time=0.874)

        # TODO 6.693 secs누구나 더 높은 가격에 팔고 더 낮은 가격에 사고 싶기 때문에 호가창에는 지정가 주문들이 쌓이기 시작합니다
        # TODO 0:00:16.204  ~  0:00:22.897
        # TODO 1.0secs pause
        # TODO 0:00:22.897  ~  0:00:23.897

        # TODO 5.629 secs그렇게 지정가 주문들이 현재가 위 아래로 계속 쌓이기만 하면 가격은 움직이지 않습니다
        # TODO 0:00:23.897  ~  0:00:29.526
        # TODO 1.0secs pause
        # TODO 0:00:29.526  ~  0:00:30.526

        # TODO 11.573 secs실제로 호가창에 100달러와 101달러가 맞닿아 있고 아무도 시장가 주문을 넣지 않으면 가격은 마지막 거래가 100원에서 매수였으면 100원, 101원에서 매도였으면 101원에 정지해있습니다
        # TODO 0:00:30.526  ~  0:00:42.099
        # TODO 1.0secs pause
        # TODO 0:00:42.099  ~  0:00:43.099

        # TODO 8.106 secs그러다가 누군가 기다림을 참지 못하고 시장가로 구매를 하면 호가창에 쌓여있던 물량이 시장가로 소화되면서 가격은 움직입니다
        # TODO 0:00:43.099  ~  0:00:51.205
        # TODO 1.0secs pause
        # TODO 0:00:51.205  ~  0:00:52.205

        # TODO 6.233 secs잘 생각해보면 모든 사람이 지정가 주문만 넣으면 아무 일도 일어나지 않고 모두 기다리기만 합니다
        # TODO 0:00:52.205  ~  0:00:58.438
        # TODO 1.0secs pause
        # TODO 0:00:58.438  ~  0:00:59.438

        self.wait(10)


class working2(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=

        '주문의 종류에 대해서 간단히 알아보겠습니다#1'
        '거래소에서 넣는 주문은 주문가격에 따라 크게 두 가지가 있습니다#1'
        '리밋 주문과 마켓 주문이고 한국어로는 지정가 주문 시장가 주문이라고 부릅니다#1'
        '지정가 주문은 말그대로 주문가격을 지정해놓는 주문이고 시장가 주문은 우리가 회를 먹을 때 싯가라고 부르듯이 그냥 그 자리에서 구할 수 있는대로 현재가격으로 즉시 체결하는 주문입니다#1'
        '이전에 들어본 스톱리밋오더, 스톱마켓오더, 트레일링스탑오더 같은 것은 이 가장 기본이 되는 두 종류에 부가적인 기능을 넣은 것입니다#1'


        '리밋 주문은 일반적으로 알고 있듯이 가격을 지정해서 그 가격에 거래하고 싶은 상대측이 나타나면 거래가 체결되는 주문입니다#1'
        '마켓 주문은 원하는 주문량을 입력하면 현재 나와있는 매물 중 가장 유리한 가격대로 주문량이 모두 충족될 때까지 거래를 합니다#1'
        '오더북에서 살펴보겠습니다#1'
        '지금 보시는 건 마켓 주문입니다#1'
        '매수 시장가 주문이면 빨간색 칸 중 가장 아래에 있는 유리한 가격 즉 싸게 팔아줄 판매자에게 구매를 합니다#1'
        '매도 시장가 주문이면 초록색 칸 중 가장 위에 있는 유리한 가격 즉 비싸게 사줄 구매자에게 판매를 합니다#1'
        '지금 보시는 건 리밋 주문입니다#1'
        '매수 지정가 주문이면 초록색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 싼 가격에 구매하려고 대기합니다#1'
        '매도 지정가 주문이면 빨간색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 비싼 가격에 판매하려고 대기합니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        plane = NumberPlane(
            x_range=(0, 20),
            y_range=(0, 10),
            x_length=16,
            y_length=9,
            axis_config={"include_numbers": False},
        )
        x_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ]
        y_list = [ 0, 1, 4, 2, 3, 7, 2, 6, 8, 6, 3, 2, 1, 2, 14, 7, 2, 6, 8, 6 ]
        # plane.center()
        line_graph = plane.plot_line_graph(
            x_values=x_list,
            y_values=y_list,
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3, fill_color=PURPLE),
            stroke_width=4,
        )

        path = VMobject()
        # graph_1_subpath = axes.plot(lambda x: (x - 1) ** 2 + 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
        # graph_1_subpath.reverse_points()
        # path.add_subpath(graph_1_subpath.get_all_points())
        # graph_2_subpath = axes.plot(lambda x: -(x - 1) ** 2 - 1, color=BLUE, x_range=[ 1, 3 ]).set_z_index(3)
        # dot_for_path = Dot(radius=0.3, color=GREEN).move_to(graph_1_b_dot)

        # print()
        # path.add_points_as_corners([ plane.c2p(x, y) for x, y in zip(x_list, y_list) ])
        # path.add_points_as_corners(graph_2_subpath.get_all_points())

        # self.play(MoveAlongPath(self.camera.frame, path), run_time=5)

        dot = Dot().move_to(plane.c2p(5, 5))
        self.play(Create(dot))
        #           MoveAlongPath(self.camera.frame, line_graph), run_time=5)
        # self.play(MoveAlongPath(self.camera.frame, path), run_time=5)

        # dot_for_path = Dot()

        # self.play(MoveAlongPath(dot_for_path, line_graph), run_time=5)

        # self.play(self.camera.frame.animate.scale(0.5).move_to(dot_for_path))


class working3(ThreeDScene):
    def imp_loss_surface(self, u, v):
        x = u
        y = v
        k = ((1 + x) / (1 + y)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        # hold_val = 0.5*x+0.5*y
        # z = np.sin(x) * np.cos(y)
        return np.array([ x, y, z ])

    def dollar_val_surface(self, u, v):
        if u + v > 3:
            v = v - (u + v - 3)

        # x = u
        # y = v
        k = ((1 + u) / (1 + v)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
        curr_val = hold_val * (1 + z) - 1

        return np.array([ u, v, curr_val ])

    def dollar_val_surface_circle(self, u, v):
        if u ** 2 + v ** 2 < 0.5 ** 2:
            # v=np.sqrt(0.5 ** 2-u ** 2)
            # return np.array([ u, v, 0 ])
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1
        else:

            angle = angle_of_vector(np.array([ u, v, 0 ]))
            u = np.cos(angle) * 0.5
            v = np.sin(angle) * 0.5
            k = ((1 + u) / (1 + v)) - 1
            z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
            hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
            curr_val = hold_val * (1 + z) - 1

        return np.array([ u, v, curr_val ])

        # x = u
        # y = v

    def construct(self):
        resolution_fa = 20
        # self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, gamma=0, zoom=1)
        axes = ThreeDAxes(x_range=(-0.99, 3, 0.33), y_range=(-0.99, 3, 0.33), z_range=(-1, 3, 1 / 3),
                          x_length=5, y_length=5, z_length=5)

        lab_x = axes.get_x_axis_label(Tex("$x$-label"))
        lab_y = axes.get_y_axis_label(Tex("$y$-label"))
        lab_z = axes.get_z_axis_label(Tex("$z$-label"))
        labs = VGroup(lab_x, lab_y, lab_z)

        imp_loss_graph = Surface(
            lambda u, v: axes.c2p(*self.imp_loss_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            fill_color=PINK
        )

        # sub_axes = ThreeDAxes(x_range=(-0.99, 3, 0.33), y_range=(-0.99, 3, 0.33), z_range=(-1, 3, 1/3),
        #                   x_length=5, y_length=5, z_length=5).shift(IN*2)
        sub_axes = Axes(x_range=(-0.99, 3, 0.33), y_range=(-0.99, 3, 0.33),
                        x_length=5, y_length=5).shift(IN * 2)

        some_graph = axes.plot(lambda x: 2 * x, x_range=[ -0.99, 2 ]).set_stroke(width=10, color=RED).set_shade_in_3d(True)

        some_graph.set_z_index_by_z_coordinate()
        entropy1 = ParametricFunction(lambda t: axes.c2p(t, t, 0), color=BLUE, stroke_width=6, t_range=[ -0.99, 3 ]).set_shade_in_3d(True)
        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface_circle(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=30
            # checkerboard_colors=[C0177, C0134]
        )

        val_graph.set_style(fill_opacity=0.5)
        val_graph.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

        # self.add(sub_axes[0:2],some_graph,entropy1)
        self.add(some_graph, entropy1)

        # imp_loss_surface = Surface(
        #     lambda u, v: axes.c2p(u, v, imp_loss_surface(u, v)),
        #     resolution=(resolution_fa, resolution_fa),
        #     v_range=[-0.9, 4],
        #     u_range=[-0.9, 4],
        #     color=PINK
        #     )
        # dollar_val_surface = Surface(
        #     lambda u, v: axes.c2p(u, v, dollar_val_surface(u, v)),
        #     resolution=(resolution_fa, resolution_fa),
        #     v_range=[-0.9, 4],
        #     u_range=[-0.9, 4],
        #     color=RED
        #     )
        #

        my_graph = axes.plot(lambda x: x, x_range=[ -1, 5 ])
        # my_graph.set_colors_by_gradient([RED,BLUE])
        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        # face = ThreeDVMobject()
        # face.set_points_as_corners([
        #     [ 1, 0, 0 ],
        #     [ 1, 0, 5 ],
        #     [ 0, 1, 5 ],
        #     [ 0, 1, 0 ],
        #     [ 1, 0, 0 ]
        # ])
        #
        # face.set_fill(color=RED, opacity=0.5)
        # face.set_stroke(color=RED_E,width=3,opacity=0.7)
        #
        three_d_wall = ThreeDVMobject().set_points_as_corners([ [ -0.5, -0.5, -0.5 ],
                                                                [ 2, -0.5, -0.5 ],
                                                                [ 2, -0.5, 1 ],
                                                                [ -0.5, -0.5, 1 ],
                                                                [ -0.5, -0.5, -0.5 ],
                                                                ]).set_fill(color=BLUE, opacity=1).set_shade_in_3d(True)

        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, labs)
        # self.add(imp_loss_graph)
        # self.play(Create(val_graph),run_time=5)
        self.add(val_graph, three_d_wall)
        # self.play(Create(my_graph))
        # self.play(my_graph.animate.set_color_by_gradient([RED,BLUE,GREEN]),run_time=3)
        # self.play(my_graph.animate.set_color(RED),run_time=3)
        # val_graph.get_z_index_reference_point()
        # some_graph.get_z_index_reference_point()

        # val_graph.set_z_index_by_z_coordinate()
        # some_graph.set_z_index_by_z_coordinate()
        # axes.set_z_index(5)
        # val_graph.set_z_index(1)
        # some_graph.set_z_index(3)
        # entropy1.set_z_index(3)
        # three_d_wall.set_z_index(8)
        # some_graph.set_z_index_by_z_coordinate()

        # some_graph.shift(IN * 3)

        # print(val_graph.get_z_index_reference_point())
        # print(some_graph.get_z_index_reference_point())
        # print(val_graph.get_z())
        # print(some_graph.get_z())
        self.set_camera_orientation(theta=-90 * DEGREES, phi=45 * DEGREES, zoom=1)

        # self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 5)
        # self.begin_ambient_camera_rotation(rate=0.2, about="theta",run_time=1)
        # self.move_camera(phi=45*DEGREES, about="phi",run_time=3)
        # self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES,gamma=0)

        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=45 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=90 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(phi=135 * DEGREES, about="phi", run_time=1)
        # self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        # self.move_camera(theta=PI / 2, about="theta", run_time=2)


class working2(ThreeDScene):
    """3디 공간 제트 엑스 와이 순 """

    def construct(self):
        axes = ThreeDAxes(x_range=[ 0, 1, 0.2 ],
                          y_range=[ 0, 1, 0.2 ],
                          z_range=[ 0, 1, 0.2 ],
                          x_length=8,
                          y_length=8,
                          z_length=8,
                          tips=False,
                          axis_config={'include_numbers': True, 'include_ticks': True, "line_to_number_buff": 0.7},
                          x_axis_config={"label_direction": D},
                          y_axis_config={"label_direction": R},
                          z_axis_config={"label_direction": IN, "line_to_number_buff": 1}
                          )

        new_axes = three_d_space_zxy(self, axes)

        self.add(new_axes)

        x_axis = new_axes[ 0 ]
        y_axis = new_axes[ 1 ]
        z_axis = new_axes[ 2 ]

        # 실제 쓸 축들만 뉴 엑시스로 정의
        # new_axes = VGroup(axes[ 0 ], axes[ 1 ], axes[ 3 ], aux_lines)
        #
        x_axis.set_color(RED)
        y_axis.set_color(GREEN)
        z_axis.set_color(BLUE)

        # 뉴엑시스는 클래스가 없이 그저 브이그룹이어서 기존의 메서드들을 사용 못 함 그래서 메서드 사용은 기존 엑시스
        # axes.get_z_axis_label('z')
        # axes.get_x_axis_label('x')
        # axes.get_y_axis_label('y')

        self.camera.set_zoom(0.6)

        # numbers = VGroup(*axes[ 0 ].numbers, *axes[ 1 ].numbers, *axes[ 3 ].numbers)

        # if Zoom is applied, gotta change scale,
        # for number in numbers:
        #     number.scale(0.5)

        self.move_camera(theta=-45 * DEGREES, about="theta", run_time=1)
        self.move_camera(phi=45 * DEGREES, about="phi", run_time=1)

        self.wait(3)


class working1(ThreeDScene):
    def dollar_val_surface(self, u, v):
        if u + v > 3:
            v = v - (u + v - 3)

        k = ((1 + u) / (1 + v)) - 1
        z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
        hold_val = 0.5 * (1 + u) + 0.5 * (1 + v)
        curr_val = hold_val * (1 + z) - 1

        return np.array([ u, v, curr_val ])

    def construct(self):
        axes = ThreeDAxes(x_range=[ -4, 4, 2 ],
                          y_range=[ -4, 4, 2 ],
                          z_range=[ -4, 4, 2 ],
                          x_length=8,
                          y_length=8,
                          z_length=8,
                          tips=False,
                          axis_config={'include_numbers': True, 'include_ticks': True, "line_to_number_buff": 0.2},
                          x_axis_config={"label_direction": DR},
                          y_axis_config={"label_direction": UL},
                          z_axis_config={"label_direction": UR, "line_to_number_buff": 0.2}

                          )

        circle = Circle()

        self.play(TracedPath)
        # self.add(text, axes)

        # self.wait(2)

        self.wait(2)

        self.wait(1)


class working2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[ 0, 1, 0.2 ],
                          y_range=[ 0, 1, 0.2 ],
                          z_range=[ 0, 1, 0.2 ],
                          x_length=8,
                          y_length=8,
                          z_length=8,
                          tips=False,
                          axis_config={'include_numbers': True, 'include_ticks': True, "line_to_number_buff": 0.7},
                          x_axis_config={"label_direction": D},
                          y_axis_config={"label_direction": R},
                          z_axis_config={"label_direction": IN, "line_to_number_buff": 0.7}
                          )

        new_axes = three_d_space_zxy(self, axes)

        self.add(new_axes)
        self.wait(1)


class working2(MovingCameraScene):

    def construct(self):
        current1 = Current(LEFT * 4)

        mag_tracker =ValueTracker(4)

        # current2 = redraw(lambda: Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))
        current2 = Current(RIGHT * 4, direction=IN, magnitude=mag_tracker.get_value())

        def mag_change(current):
            current.magnitude = mag_tracker.get_value()

        current2.add_updater(mag_change)
        magnet = BarMagnet().rotate(PI / 4)

        # field = redraw(lambda: MagneticField(current1, current2, magnet))

        # field = MagneticField(current1, current2)
        field.add_updater(lambda field:field.become(MagneticField(current1, Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))))


        self.add(field, current1, current2, magnet)


        # self.play(field.animate.shift(L*1))

        # self.wait(5)

        self.play(current1.animate.shift(L * 2))
        # self.play(current2.animate.become(Current(U * 2.5, direction=IN, magnitude=10)))

        self.play(mag_tracker.animate.set_value(10))

        # self.play()
        self.play(magnet.animate.rotate(PI / 4))
        # self.wait(5)
        self.wait(2)
#

class working2(SpaceScene):

    def construct(self):
        circle = Circle().shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)

        tri = Triangle().shift(UP+L*1)
        tri.set_fill(BLUE, 1)
        # circle.shift(DOWN + RIGHT)


        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)

        ground = Line([ -4, -4, 0 ], [ 4, -4, 0 ])
        wall1 = Line([ -4, -4, 0 ], [ -4, 4, 0 ])
        wall2 = Line([ 4, -4, 0 ], [ 4, 4, 0 ])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(rect),
            DrawBorderThenFill(tri),
        )
        self.make_rigid_body(rect, elasticity=1.2,)  # Mobjects will move with gravity
        self.make_rigid_body(tri, elasticity=0.8,)  # Mobjects will move with gravity
        self.make_rigid_body(circle, elasticity=0.3, )  # Mobjects will move with gravity
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(8)


#

# with tempconfig({"quality": "medium_quality", "preview": True, 'fps': '10',
#                  'renderer': 'opengl', 'write_to_movie': True}):
#     scene = working2()
#     #     #     # scene = working2()
#     #     #     # scene = working3()
#     #     #     # scene = working4()
#     #     #     # scene = working5()
#     scene.render()
#
# 리드로우 매크로 브이그룹
