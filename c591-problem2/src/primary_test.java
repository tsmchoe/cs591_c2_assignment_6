import org.junit.Test;
import static org.junit.Assert.assertEquals;




public class primary_test {

    /*
        Test the answerQuestion, I used this to test that the primary function works.
        Since there is a problem with testing a scanner input
     */
    @Test
    public void test() throws Exception{
        assertEquals("Please enter a Circle, Square or Rectangle", problem_2.answerQuestion("K"));
        assertEquals( null, problem_2.answerQuestion("C"));

    }

}
