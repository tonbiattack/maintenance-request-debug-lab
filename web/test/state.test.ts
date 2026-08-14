import assert from 'node:assert/strict'
import test from 'node:test'
import { openCompletionForm } from '../src/formState.js'
import { requestKeys } from '../src/queryKeys.js'
test('M02: request list cache keys distinguish status and page', () => { assert.notDeepEqual(requestKeys.list('OPEN', 1), requestKeys.list('COMPLETED', 1)); assert.notDeepEqual(requestKeys.list('OPEN', 1), requestKeys.list('OPEN', 2)) })
test('M12: completion form is bound to the currently opened request', () => { assert.equal(openCompletionForm('req-b').requestId, 'req-b') })
