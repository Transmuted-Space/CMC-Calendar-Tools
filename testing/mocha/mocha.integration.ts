import './mocha.unit'
import { use } from 'chai'
import chaiAsPromised = require('chai-as-promised')

process.env.E2E_API_TARGET =
  process.env.E2E_API_TARGET || 'http://localhost:9999'
use(chaiAsPromised)
