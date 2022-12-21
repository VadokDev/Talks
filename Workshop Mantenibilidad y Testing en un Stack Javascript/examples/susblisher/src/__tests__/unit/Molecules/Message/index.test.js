import Message from '../../../../molecules/Message';
import { render, screen, fireEvent } from '@testing-library/react';

describe('Message molecule unit testing', () => {
  it('Should render a message with the given content', () => {
    const expectedContent = 'Hola';
    render(<Message content={expectedContent} />);
    expect(screen.getByText(expectedContent)).toBeInTheDocument();
  });

  it('Should call the handler when the button is clicked', () => {
    const buttonText = 'Click me';
    const onClickHandlerSpy = jest.fn();

    render(<Message content={buttonText} onClickHandler={onClickHandlerSpy} />);
    const button = screen.getByText(buttonText);
    fireEvent.click(button);

    expect(onClickHandlerSpy).toBeCalled();
  });
});
