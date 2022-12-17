import { render, screen } from '@testing-library/react';
import App from '../../App';

describe('App unit testing suite', () => {
  it('Should render the list of messages', () => {
    render(<App />);
    const message = screen.getByText('Walmart');
    expect(message).toBeInTheDocument();
  });
});
