
const calculateWeight = (earthWeight, planet) => {
    switch (planet){
      case 'Mercury':
        return earthWeight * 0.378;
        break;
      case 'Venus':
        return earthWeight * 0.907;
        break;
      case 'Mars':
        return earthWeight * 0.377;
        break;
      case 'Jupiter':
        return earthWeight * 2.36;
        break;
      case 'Saturn':
        return earthWeight * 0.916;
        break;
      default:
        return 'Invalid Planet Entry. Try: Mercury, Venus, Mars, Jupiter, or Saturn.';
        break;
  
    }
  }
  
  
  