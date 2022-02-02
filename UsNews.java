package j.ucdavis21.w3;

/*
 * Jörn Boehnke 2022
 */

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class UsNews {
    
    public static void main(String[] args) throws IOException, InterruptedException {
        
        Document doc = Jsoup.connect("https://www.usnews.com/")
                            .userAgent("Mozilla/5.0")
                            .get();
        
        Element h2 = doc.selectFirst("h2:contains(Top Stories)");
        Elements links = h2.nextElementSibling().select("a");
        
        /*
         * the following line of code was used to realize that Top Story links to one story come in
         * pairs of 3
         */
//        links.forEach(l -> System.out.println(l.attr("href")));
        
        String url2ndTopStory = links.get(3).attr("href"); // Java indices start with 0
        System.out.println(url2ndTopStory);
        
        /*
         * wait 5 seconds before we access US News' servers again
         */
        Thread.sleep(5_000);
        
        Document docTopStory = Jsoup.connect(url2ndTopStory)
                                    .userAgent("Mozilla/5.0")
                                    .get();
        
        String title = docTopStory.select("h1").text();
        String content = docTopStory.select("#main-column").text();
        String[] sentences = content.split("\\.");
        /*
         * deal with "(... Images)"
         */
        
        System.out.println(title);
//        System.out.println(content);
        System.out.println(sentences[1].trim() + ". " + sentences[2].trim() + ". " + sentences[3].trim() + ".");
        
    }
    
}
