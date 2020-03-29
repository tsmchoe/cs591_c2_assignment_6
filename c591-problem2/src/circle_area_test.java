import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class circle_area_test {
    @Test
    public void test() throws Exception{
        assertEquals(null, problem_2.circleArea(-1.0));
        assertEquals(null, problem_2.circleArea(-1.0));
        assertEquals(0, problem_2.circleArea(0.0),1);
        assertEquals(28.27, problem_2.circleArea(3.0),1);
    }

}
