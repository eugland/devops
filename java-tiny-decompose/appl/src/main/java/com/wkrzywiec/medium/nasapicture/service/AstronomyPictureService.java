package com.wkrzywiec.medium.nasapicture.service;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

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

    public AstronomyPictureOfDay getDescription() {
        return restTemplate.getForObject(
                "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&hd&date="+getYesterdayDateString(),
                AstronomyPictureOfDay.class);
    }

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

    private Date yesterday() {
        final Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DATE, -1);
        return cal.getTime();
    }
    
    private String getYesterdayDateString() {
            DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
            return dateFormat.format(yesterday());
    }
}
