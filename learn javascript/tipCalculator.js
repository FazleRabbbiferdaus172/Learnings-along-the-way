const tipCalculator = (quality, total) => {
    switch (quality){
      case 'bad':
        return (total*5)/100;
        break;
        case 'ok':
        return (total*15)/100;
        break;
        case 'good':
        return (total*20)/100;
        break;
        case 'excellent':
        return (total*30)/100;
        break;
        default:
        return (total*18)/100;
        break;
    }
  }
  