import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class circle_perimeter_test {
    @Test
    public void test() throws Exception{
        assertEquals(null, problem_2.circlePerimeter(-1.0));
        assertEquals(null, problem_2.circlePerimeter(-1.0));
        assertEquals(0, problem_2.circlePerimeter(0.0),1);
        assertEquals(18.85, problem_2.circlePerimeter(3.0),1);
    }

}