package hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMethod;


@SpringBootApplication
@RestController
public class Application {

    @CrossOrigin(origins = "*")
    @RequestMapping("/hi")
    public String home() {
        return "Hello Docker from Java!";
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}
