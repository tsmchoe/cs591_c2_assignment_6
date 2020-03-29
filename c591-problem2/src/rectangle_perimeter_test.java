import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class rectangle_perimeter_test {

    @Test
    public void test() throws Exception{
        assertEquals(null, problem_2.rectanglePerimeter(-2.0, 6.0));
        assertEquals(null, problem_2.rectanglePerimeter(-2.0, -6.0));
        assertEquals(null, problem_2.rectanglePerimeter(2.0, -6.0));
        assertEquals(14, problem_2.rectanglePerimeter(2.0, 5.0) , 1);
        assertEquals(28, problem_2.rectanglePerimeter(8.0, 6.0) , 1);
        assertEquals(34, problem_2.rectanglePerimeter(10.0, 7.0) , 1);
        assertEquals(30, problem_2.rectanglePerimeter(8.0, 7.0) , 1);
        assertEquals(24, problem_2.rectanglePerimeter(8.0, 4.0) , 1);
        assertEquals(38, problem_2.rectanglePerimeter(10.0, 9.0) , 1);
    }
}
