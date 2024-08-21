```csharp
namespace Project.Application.UseCases.Brands.GetBrandById.Behaviors
{
    public class GetBrandByIdAuthorizationBehavior : IPipelineBehavior<GetBrandByIdQuery, GetBrandByIdDto>
    {
        private readonly IAuthorizationService _authorizationService;

        public GetBrandByIdAuthorizationBehavior(IAuthorizationService authorizationService)
        {
            _authorizationService = authorizationService;
        }

        public async Task<GetBrandByIdDto> Handle(GetBrandByIdQuery query, RequestHandlerDelegate<GetBrandByIdDto> next, CancellationToken ct = default)
        {
            var user = await _authorizationService.GetUserAsync() ??
                throw new UnauthorizedAccessException("User has no authorization to execute this request!");

            return await next();
        }
    }
}
```