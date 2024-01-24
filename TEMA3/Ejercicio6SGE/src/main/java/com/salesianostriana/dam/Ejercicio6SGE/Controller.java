package com.salesianostriana.dam.Ejercicio6SGE;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {

    @GetMapping("/HolaMundo")
    public String holaMundo (){

        return "Hola Mundo";
    }
}
