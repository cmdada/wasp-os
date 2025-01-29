# SPDX-License-Identifier: MY-LICENSE
# Copyright (C) YEAR(S), AUTHOR

import wasp

class HelloApp():
    """A scrolling vocabulary app for wasp-os."""
    NAME = "Hello"

    def __init__(self):
        self.vocab = [
            "1. el bienestar - well-being",
            "2. la droga - drug",
            "3. el/la drogadicto/a - drug addict",
            "4. el masaje - massage",
            "5. el/la teleadicto/a - couch potato",
            "6. adelgazar - to lose weight; to slim down",
            "7. aliviar el estrés - to reduce stress",
            "8. aliviar la tensión - to reduce tension",
            "9. apurarse, darse prisa - to hurry; to rush",
            "10. aumentar de peso, engordar - to gain weight",
            "11. disfrutar (de) - to enjoy; to reap the benefits (of)",
            "12. estar a dieta - to be on a diet",
            "13. (no) fumar - (not) to smoke",
            "14. llevar una vida sana - to lead a healthy lifestyle",
            "15. sufrir muchas presiones - to be under a lot of pressure",
            "16. tratar de (+ inf.) - to try (to do something)",
            "17. activo/a - active",
            "18. débil - weak",
            "19. en exceso - in excess",
            "20. flexible - flexible",
            "21. fuerte - strong",
            "22. sedentario/a - sedentary",
            "23. tranquilo/a - calm; quiet",
            "24. la cinta caminadora - treadmill",
            "25. la clase de ejercicios aeróbicos - aerobics class",
            "26. el/la entrenador(a) - trainer",
            "27. el músculo - muscle",
            "28. calentarse (e:ie) - to warm up",
            "29. entrenarse - to train",
            "30. estar en buena forma - to be in good shape",
            "31. hacer ejercicio - to exercise",
            "32. hacer ejercicios aeróbicos - to do aerobics",
            "33. hacer ejercicios de estiramiento - to do stretching exercises",
            "34. hacer gimnasia - to work out",
            "35. levantar pesas - to lift weights",
            "36. mantenerse en forma - to stay in shape",
            "37. sudar - to sweat",
            "38. la bebida alcohólica - alcoholic beverage",
            "39. la cafeína - caffeine",
            "40. la caloría - calorie",
            "41. el colesterol - cholesterol",
            "42. la grasa - fat",
            "43. la merienda - afternoon snack",
            "44. el mineral - mineral",
            "45. la nutrición - nutrition",
            "46. el/la nutricionista - nutritionist",
            "47. la proteína - protein",
            "48. la vitamina - vitamin",
            "49. comer una dieta equilibrada - to eat a balanced diet",
            "50. consumir alcohol - to consume alcohol",
            "51. descafeinado/a - decaffeinated"
        ]
        self.offset = 0  # Scroll position
        wasp.system.request_event(wasp.EventMask.TOUCH)  # Enable touch events

    def foreground(self):
        self._draw()

    def _draw(self):
        draw = wasp.watch.drawable
        draw.fill()
        
        # Display up to 5 lines at a time
        max_lines = 5
        for i in range(max_lines):
            if self.offset + i < len(self.vocab):
                draw.string(self.vocab[self.offset + i], 0, 20 * i, width=240)

    def touch(self, event):
        """Handle tap event to scroll down."""
        if event[0] == wasp.EventType.TOUCH:
            self.scroll_down()

    def scroll_down(self):
        """Scroll down or loop back to the top."""
        if self.offset < len(self.vocab) - 5:
            self.offset += 1
        else:
            self.offset = 0  # Loop back to the beginning
        self._draw()
