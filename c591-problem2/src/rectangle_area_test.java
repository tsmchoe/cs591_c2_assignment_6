import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class rectangle_area_test {

    @Test
    public void test() throws Exception{
        assertEquals(null, problem_2.rectangleArea(-2.0, 6.0));
        assertEquals(null, problem_2.rectangleArea(-2.0, -6.0));
        assertEquals(null, problem_2.rectangleArea(2.0, -6.0));
        assertEquals(10, problem_2.rectangleArea(2.0, 5.0) , 1);
        assertEquals(48, problem_2.rectangleArea(8.0, 6.0) , 1);
        assertEquals(70, problem_2.rectangleArea(10.0, 7.0) , 1);
        assertEquals(56, problem_2.rectangleArea(8.0, 7.0) , 1);
        assertEquals(32, problem_2.rectangleArea(8.0, 4.0) , 1);
        assertEquals(90, problem_2.rectangleArea(10.0, 9.0) , 1);
    }
}
