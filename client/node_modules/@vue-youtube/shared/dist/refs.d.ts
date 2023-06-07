import type { Ref, ComponentPublicInstance } from 'vue-demi';
export declare type MaybeRef<T> = T | Ref<T>;
export declare type MaybeElementRef = MaybeRef<HTMLElement | ComponentPublicInstance | undefined | null>;
export declare function unrefElement(ref: MaybeElementRef): HTMLElement | undefined;
