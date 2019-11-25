package com.wkrzywiec.medium.nasapicture.service;

<<<<<<< HEAD
=======
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

>>>>>>> e9d04d9c1083635e4a429eb3738bbf3f16bb66ed
import com.wkrzywiec.medium.nasapicture.model.AstronomyPictureOfDay;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AstronomyPictureService {

    @Autowired
    private RestTemplate restTemplate;

    public AstronomyPictureOfDay getTodayPicture() {
        return restTemplate.getForObject(
                "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&hd",
                AstronomyPictureOfDay.class);
    }

<<<<<<< HEAD
=======
    public AstronomyPictureOfDay getDescription() {
        return restTemplate.getForObject(
                "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&hd&date="+getYesterdayDateString(),
                AstronomyPictureOfDay.class);
    }

>>>>>>> e9d04d9c1083635e4a429eb3738bbf3f16bb66ed
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
<<<<<<< HEAD
=======

    private Date yesterday() {
        final Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DATE, -1);
        return cal.getTime();
    }
    
    private String getYesterdayDateString() {
            DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
            return dateFormat.format(yesterday());
    }
>>>>>>> e9d04d9c1083635e4a429eb3738bbf3f16bb66ed
}
