import Message from '../../../../molecules/Message';
import { render, screen } from '@testing-library/react';
describe('Message molecule unit testing', () => {
  it('Should render a message with the given content', () => {
    const expectedContent = 'Hola';
    render(<Message content={expectedContent} />);
    expect(screen.getByText(expectedContent)).toBeInTheDocument();
  });
});
